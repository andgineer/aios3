"""S3 "files" operations with aiobotocore."""

import io
from typing import IO, AsyncGenerator, Optional

from aiobotocore.session import AioBaseClient, get_session
from botocore.exceptions import ClientError

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

    Raises:
        ClientError: If S3 operation fails.
    """
    if s3 is not None:
        await s3.put_object(Body=body, Bucket=bucket, Key=key)
    else:
        session = get_session()
        async with session.create_client("s3") as temp_s3:
            await temp_s3.put_object(Body=body, Bucket=bucket, Key=key)


async def read(  # pylint: disable= invalid-name
    bucket: str,
    key: str,
    chunk_size: Optional[int] = None,
    s3: Optional[AioBaseClient] = None,
) -> bytes:
    """Read the full content of the file as bytes.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        chunk_size: max number of bytes to read in one chunk. by default read all.
        s3: boto s3 client. by default it auto-created inside the function.

    Return:
        The file content as bytes.

    Raises:
        FileNotFoundError: If the S3 object does not exist.
        ClientError: If other S3 operation fails.
    """
    return b"".join(
        [
            chunk
            async for chunk in chunks(
                bucket=bucket, key=key, chunk_size=chunk_size, s3=s3
            )
        ]
    )


async def chunks(  # pylint: disable= invalid-name
    bucket: str,
    key: str,
    chunk_size: Optional[int] = None,
    s3: Optional[AioBaseClient] = None,
) -> AsyncGenerator[bytearray, None]:
    """Generate file chunks `chunk_size` bytes max.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        chunk_size: max number of bytes to read in one chunk. by default read file as one chunk.
        s3: boto s3 client. by default it auto-created inside the function.

    Return:
        Chunks of the file.

    Raises:
        FileNotFoundError: If the S3 object does not exist.
        ClientError: If other S3 operation fails.
    """
    try:
        if s3 is not None:
            s3_file_obj = await s3.get_object(Bucket=bucket, Key=key)
        else:
            session = get_session()
            async with session.create_client("s3") as temp_s3:
                s3_file_obj = await temp_s3.get_object(Bucket=bucket, Key=key)

        s3_file_stream = s3_file_obj["Body"]
        try:
            while True:
                chunk = await s3_file_stream.read(chunk_size)
                if len(chunk) == 0:
                    break
                yield chunk
        finally:
            s3_file_stream.close()
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchKey":
            raise FileNotFoundError(f"S3 object not found: s3://{bucket}/{key}") from e
        raise


async def stream(  # pylint: disable= invalid-name
    bucket: str,
    key: str,
    chunk_size: Optional[int] = None,
    s3: Optional[AioBaseClient] = None,
) -> IO[bytes]:
    """Create file-like object to stream the file content.

    Note: This function loads all chunks into memory to create a synchronous stream.
    For true streaming without loading all data into memory, use the chunks() function directly.

    Args:
        bucket: S3 bucket.
        key: path in the bucket including "file name".
        chunk_size: max number of bytes to read in one chunk. by default read file as one chunk.
        s3: boto s3 client. by default it auto-created inside the function.

    Return:
        Python file stream with the file content.

    Raises:
        FileNotFoundError: If the S3 object does not exist.
        ClientError: If other S3 operation fails.
    """
    # Note: We must collect all chunks into memory because StreamFromIter expects
    # a synchronous iterator, but our chunks() function is an async generator.
    # For memory-efficient streaming, use chunks() directly instead of stream().
    file_chunks = [
        chunk
        async for chunk in chunks(bucket=bucket, key=key, chunk_size=chunk_size, s3=s3)
    ]
    return io.BufferedReader(StreamFromIter(file_chunks))
