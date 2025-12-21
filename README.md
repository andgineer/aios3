[![Build Status](https://github.com/andgineer/aios3/workflows/ci/badge.svg)](https://github.com/andgineer/aios3/actions)
[![Coverage](https://raw.githubusercontent.com/andgineer/aios3/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/andgineer/aios3/blob/python-coverage-comment-action-data/htmlcov/index.html)
# File-like object for aiobotocore to read from AWS S3 by chunks

aioS3 provides a file-like interface for reading large files from AWS S3 in chunks using aiobotocore.

This enables efficient memory management when working with operations that expect file-like objects, such as
`pickle.load()` or `json.load()`, without loading entire files into memory.

With [stream](https://andgineer.github.io/aios3/reference/#aios3.file.stream) you can create file-like object
to read from [aiobotocore](https://aiobotocore.readthedocs.io/en/latest/) "files" by chunks.

# Documentation
- [aioS3](https://andgineer.github.io/aios3/)
- [blog](https://sorokin.engineer/posts/en/aws_s3_chunks_async.html)

# Developers

Do not forget to run `. ./activate.sh`.

# Scripts
    make help

## Coverage report
* [Codecov](https://app.codecov.io/gh/andgineer/aios3/tree/master/src%2Faios3)
* [Coveralls](https://coveralls.io/github/andgineer/aios3)

> Created with cookiecutter using [template](https://github.com/andgineer/cookiecutter-python-package)
