# aioS3

File-like interface for AWS S3 with aiobotocore.

## What

- `stream()` — file-like object for chunked reading
- `read()` — read entire file as bytes
- `chunks()` — async generator for file chunks
- `save()` — write bytes to S3

## What for

Use with file-like operations (`pickle.load()`, `json.load()`, etc.) on S3 objects without loading entire files into memory.

[Detailed blog post](https://sorokin.engineer/posts/en/aws_s3_chunks_async.html)
