[![Build Status](https://github.com/andgineer/aios3/workflows/ci/badge.svg)](https://github.com/andgineer/aios3/actions)
# File-like object for aiobotocore

[stream](https://andgineer.github.io/aios3/docstrings/file/#function-stream) creates file-like object
to read from [aiobotocore](https://aiobotocore.readthedocs.io/en/latest/) by chunks.

# Documentation

[aioS3](https://andgineer.github.io/aios3/)

# Developers

Do not forget to run `. ./activate.sh`.

# Python github project template

You can use this repository as template for your Python projects.

It brings:

- Python virtual environment (see `activate.sh`)
- pre-commit configuration with mypy, flake8, black and docstrings linter (see `.pre-commit-config.yaml`)
- github pages documentation generated from written by you md-files and docstrings (see `.github/workflows/docs.yml`)
- pytest with examples of async tests and fixtures (see `tests/`)
- github actions to linter, test and to create github pages (see `.github/workflows/`)
- versions in git tags (see `verup.sh`)
- publishing Python package on pypi (see `upload.sh`)
