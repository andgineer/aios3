[![Build Status](https://github.com/andgineer/aios3/workflows/ci/badge.svg)](https://github.com/andgineer/aios3/actions)
# File-like object for aiobotocore

With [stream](https://andgineer.github.io/aios3/docstrings/file/#function-stream) you can create file-like object
to read from [aiobotocore](https://aiobotocore.readthedocs.io/en/latest/) "files" by chunks.

# Documentation

[aioS3](https://andgineer.github.io/aios3/)

# Developers

Do not forget to run `. ./activate.sh`.

# Python github project template

You can use this repository as template for your Python projects.

It brings:

- Python virtual environment (see `activate.sh`)
- pre-commit configuration with mypy, flake8, black and docstrings linter (see `.pre-commit-config.yaml`, [install pre-commit](https://pre-commit.com) and activate it with `pre-commit install`)
- github pages: [read the article](https://sorokin.engineer/posts/en/github-pages-lazydocs-mkdocs.html), the site generated from md-files in `docs/`, `docs/docstrings/` is autogenerated from source code docstrings (see `.github/workflows/docs.yml`)
- pytest with examples of async tests and fixtures (see `tests/`)
- github actions to linter, test and to create github pages (see `.github/workflows/`)
- versions in git tags (see `verup.sh`)
- publishing Python PIP package [read the article](https://sorokin.engineer/posts/en/github-actions-release-pypi-python-package.html), automatically on git tag, also creates github release with link to the version on pypi.org
- pinning dependencies versions using [pip-tools](https://github.com/jazzband/pip-tools/) (see `scripts/compile_requirements.sh`)

# Scripts
    make help
