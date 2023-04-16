import os.path

import botocore.stub
import pytest

from aios3.file import chunks, read, save, stream


class Stream:
    def __init__(self, file_content):
        self.file_content = file_content

    async def read(self, amt):
        if self.file_content is None:
            return b""
        if amt is None:
            result = self.file_content
            self.file_content = None
            return result
        result, self.file_content = self.file_content[:amt], self.file_content[amt:]
        return result

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
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_content, chunk_size
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object",
        {"Body": Stream(file_content)},
        expected_params={"Bucket": bucket, "Key": key},
    )
    assert [
        chunk async for chunk in chunks(s3=s3_stub.client, bucket=bucket, key=key, amt=chunk_size)
    ] == [
        file_content[chunk_idx : chunk_idx + chunk_size]
        for chunk_idx in range(0, len(file_content), chunk_size)
    ]


@pytest.mark.asyncio
async def test_aios3_file_stream(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_content, chunk_size
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object",
        {"Body": Stream(file_content)},
        expected_params={"Bucket": bucket, "Key": key},
    )
    assert (
        await stream(s3=s3_stub.client, bucket=bucket, key=key, amt=chunk_size)
    ).read() == file_content


@pytest.mark.asyncio
async def test_aios3_file_chunks_default_chunk_size(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_content
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object",
        {"Body": Stream(file_content)},
        expected_params={"Bucket": bucket, "Key": key},
    )
    assert [
        chunk
        async for chunk in chunks(
            s3=s3_stub.client,
            bucket=bucket,
            key=key,
        )
    ] == ([file_content] if file_content else [])


@pytest.mark.asyncio
async def test_aios3_file_read_default_chunk_size(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_content
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object",
        {"Body": Stream(file_content)},
        expected_params={"Bucket": bucket, "Key": key},
    )
    assert (
        await read(
            s3=s3_stub.client,
            bucket=bucket,
            key=key,
        )
        == file_content
    )


@pytest.mark.asyncio
async def test_aios3_file_stream_default_chunk_size(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_content
):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object",
        {"Body": Stream(file_content)},
        expected_params={"Bucket": bucket, "Key": key},
    )
    assert (
        await stream(
            s3=s3_stub.client,
            bucket=bucket,
            key=key,
        )
    ).read() == file_content


@pytest.mark.asyncio
async def test_aios3_file_read(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, file_content, chunk_size
):
    await check_reading(bucket, chunk_size, file_content, s3_file_name, s3_folder, s3_stub)


@pytest.mark.asyncio
async def test_aios3_file_read_zero_length(
    s3_stub: botocore.stub.Stubber, bucket, s3_file_name, s3_folder, chunk_size
):
    file_content = b""
    await check_reading(bucket, chunk_size, file_content, s3_file_name, s3_folder, s3_stub)


async def check_reading(bucket, chunk_size, file_content, s3_file_name, s3_folder, s3_stub):
    key = os.path.join(s3_folder, s3_file_name)
    s3_stub.add_response(
        "get_object",
        {"Body": Stream(file_content)},
        expected_params={"Bucket": bucket, "Key": key},
    )
    assert await read(s3=s3_stub.client, bucket=bucket, key=key, amt=chunk_size) == file_content
