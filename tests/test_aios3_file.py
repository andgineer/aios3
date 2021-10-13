import os.path

import botocore.stub
import pytest

from aios3.file import chunks, read, save, stream


class Stream:
    chunks_counter = 0

    def __init__(self, file_chunks):
        self.file_chunks = file_chunks

    async def read(self):
        if self.chunks_counter < len(self.file_chunks):
            self.chunks_counter += 1
            return self.file_chunks[self.chunks_counter - 1]
        return b""

    def close(self):
        pass


@pytest.mark.asyncio
async def test_aios3_file_save(s3_stub: botocore.stub.Stubber, bucket, s3_file_name):
    body = b"123"
    folder = "/456"
    key = os.path.join(folder, s3_file_name)
    s3_stub.add_response(
        "put_object", {}, expected_params={"Body": body, "Bucket": bucket, "Key": key}
    )
    await save(s3=s3_stub.client, bucket=bucket, key=key, body=body)


@pytest.mark.asyncio
async def test_aios3_file_chunks(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_chunks
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object", {"Body": Stream(file_chunks)}, expected_params={"Bucket": bucket, "Key": key}
    )
    assert [
        chunk
        async for chunk in chunks(
            s3=s3_stub.client,
            bucket=bucket,
            key=key,
        )
    ] == file_chunks


@pytest.mark.asyncio
async def test_aios3_file_read(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_chunks
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object", {"Body": Stream(file_chunks)}, expected_params={"Bucket": bucket, "Key": key}
    )
    assert (
        await read(
            s3=s3_stub.client,
            bucket=bucket,
            key=key,
        )
        == b"".join(file_chunks)
    )


@pytest.mark.asyncio
async def test_aios3_file_stream(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_chunks
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object", {"Body": Stream(file_chunks)}, expected_params={"Bucket": bucket, "Key": key}
    )
    assert (
        await stream(
            s3=s3_stub.client,
            bucket=bucket,
            key=key,
        )
    ).read() == b"".join(file_chunks)
