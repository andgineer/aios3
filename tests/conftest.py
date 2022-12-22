"""
pytest fixture configurations
"""
import os
import random
import string
from unittest.mock import patch

import aiobotocore
import aiobotocore.session
import botocore.stub
import pytest
import pytest_asyncio

MAX_FILE_LENGTH = 16
MAX_FILE_CHUNK_NUMBER = 4
S3_NAME_ALPHABET = string.ascii_letters + string.digits + "-_"
FILE_BODY_ALPHABET = (string.ascii_letters + string.digits + "-_").encode()
S3_BUCKET_NAME_LENGTH = 12
S3_FILE_FOLDER_LENGTH = 12
S3_FILE_NAME_LENGTH = 12


@pytest_asyncio.fixture(scope="function")
async def s3_stub() -> botocore.stub.Stubber:
    # to test aiobotocore we cannot use moto
    with patch.dict(os.environ, {"AWS_ACCESS_KEY_ID": "fake", "AWS_SECRET_ACCESS_KEY": "fake"}):
        session = aiobotocore.session.get_session()
        async with session.create_client("s3") as stubbed_client:
            with botocore.stub.Stubber(stubbed_client) as stubber:
                yield stubber
                stubber.assert_no_pending_responses()


@pytest.fixture(scope="function")
def file_content() -> bytes:
    return b"".join(
        random.choice(FILE_BODY_ALPHABET).to_bytes(1, "big")
        for _ in range(random.randint(0, MAX_FILE_LENGTH))
    )


@pytest.fixture(scope="function")
def chunk_size() -> int:
    return random.randint(1, MAX_FILE_LENGTH)


@pytest.fixture(scope="function")
def bucket() -> str:
    return "".join(random.choice(S3_NAME_ALPHABET) for _ in range(S3_BUCKET_NAME_LENGTH))


@pytest.fixture(scope="function")
def s3_file_name() -> str:
    return "".join(random.choice(S3_NAME_ALPHABET) for _ in range(S3_FILE_NAME_LENGTH))


@pytest.fixture(scope="function")
def s3_folder() -> str:
    return "".join(random.choice(S3_NAME_ALPHABET) for _ in range(S3_FILE_FOLDER_LENGTH))
