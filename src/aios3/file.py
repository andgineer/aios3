"""S3 "files" operations with aiobotocore."""
import contextlib
import io
from typing import IO, AsyncGenerator, Optional

from aiobotocore.session import AioBaseClient, get_session

from aios3.stream_iter import StreamFromIter


async def save(  # pylint: disable= invalid-name
    bucket: str, key: str, body: bytes, s3: Optional[AioBaseClient] = None
) -> None:
    """Create the file with the `body`.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        body: content to write into file.
        s3: boto s3 client. by default it auto-created inside the function.
    """
    session = get_session() if s3 is None else None
    async with session.create_client(
        "s3"
    ) if s3 is None else contextlib.AsyncExitStack() as s3_temp:
        await (s3 or s3_temp).put_object(Body=body, Bucket=bucket, Key=key)


async def read(  # pylint: disable= invalid-name
    bucket: str, key: str, amt: Optional[int] = None, s3: Optional[AioBaseClient] = None
) -> bytes:
    """Read the full content of the file as bytes.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        amt: max number of bytes to read in one chunk. by default read all.
        s3: boto s3 client. by default it auto-created inside the function.

    Return:
        The file content as bytes.
    """
    return b"".join([chunk async for chunk in chunks(bucket=bucket, key=key, amt=amt, s3=s3)])


async def chunks(  # pylint: disable= invalid-name
    bucket: str, key: str, amt: Optional[int] = None, s3: Optional[AioBaseClient] = None
) -> AsyncGenerator[bytearray, None]:
    """Generate file chunks `amt` bytes max.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        amt: max number of bytes to read in one chunk. by default read file as one chunk.
        s3: boto s3 client. by default it auto-created inside the function.

    Return:
        Chunks of the file.
    """
    session = get_session() if s3 is None else None
    async with session.create_client(
        "s3"
    ) if s3 is None else contextlib.AsyncExitStack() as s3_temp:
        s3_file_obj = await (s3 or s3_temp).get_object(Bucket=bucket, Key=key)
        s3_file_stream = s3_file_obj["Body"]
        chunks_count = 0
        try:
            while True:
                chunk = await s3_file_stream.read(amt)
                chunks_count += 1
                if len(chunk) == 0:
                    break
                yield chunk
        finally:
            s3_file_stream.close()


async def stream(  # pylint: disable= invalid-name
    bucket: str, key: str, amt: Optional[int] = None, s3: Optional[AioBaseClient] = None
) -> IO[bytes]:
    """Create file-like object to stream the file content.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        amt: max number of bytes to read in one chunk. by default read file as one chunk.
        s3: boto s3 client. by default it auto-created inside the function.

    Return:
        Python file stream with the file content.
    """
    file_chunks = [chunk async for chunk in chunks(bucket=bucket, key=key, amt=amt, s3=s3)]
    return io.BufferedReader(StreamFromIter(file_chunks))
