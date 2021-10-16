[![Build Status](https://github.com/andgineer/aios3/workflows/ci/badge.svg)](https://github.com/andgineer/aios3/actions)
# Asyncio S3 file operations

Wrap [aiobotocore](https://aiobotocore.readthedocs.io/en/latest/) to simplify reading of large files.
aiobotocore read them in chunks and with aioS3 you do not have to write reading loops, just use simple functions
like [read](https://andgineer.github.io/aios3/api-reference/file/#function-read) for example

# Documentation

[aioS3](https://andgineer.github.io/aios3/)

#### note for myself

Do not forget to set git branch `gh-pages` as source for github pages.
This branch auto-updated by `mkdocs gh-deploy` in github actions.
