# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

aios3 is a Python library that provides file-like objects for reading AWS S3 files by chunks using aiobotocore. The main functionality is creating streamable interfaces to S3 objects for asynchronous operations.

## Development Environment Setup

The project uses UV for dependency management and virtual environment handling:

```bash
# Source the activation script to set up or activate the development environment
. ./activate.sh
```

This script:
- Creates a virtual environment using Python 3.11 if it doesn't exist
- Activates the virtual environment
- Installs dependencies with `uv sync --frozen`

## Common Development Commands

### Testing
```bash
# Run all tests with pytest (use python -m pytest for proper module loading)
python -m pytest -v

# Run tests with coverage
python -m pytest --cov

# Run specific test file
python -m pytest tests/test_aios3_file.py -v

# Tests include doctests (configured in pytest.ini)
```

### Code Quality
```bash
# Run pre-commit hooks (includes ruff, mypy, pylint)
pre-commit run --all-files

# Individual tools:
ruff check --fix          # Linting and formatting
mypy src/                 # Type checking
pylint src/               # Additional linting
```

### Documentation
```bash
# Build and serve English documentation
make docs

# Build and serve Russian documentation  
make docs-ru
```

### Version Management
```bash
# Bump version for bug fix
make ver-bug

# Bump version for feature
make ver-feature

# Bump version for release
make ver-release
```

### Dependency Management
```bash
# Upgrade all dependencies including pre-commit hooks
make reqs
```

## Code Architecture

### Core Components

- **`src/aios3/file.py`** - Main module containing S3 file operations:
  - `save()` - Save bytes to S3 object
  - `read()` - Read full S3 object content
  - `chunks()` - Generate S3 object chunks asynchronously
  - `stream()` - Create file-like object for S3 content

- **`src/aios3/stream_iter.py`** - Contains `StreamFromIter` class that implements Python's io stream protocol to convert iterables/iterators into file-like objects

### Key Design Patterns

- All functions accept optional `s3` client parameter - if None, creates temporary client using aiobotocore session
- Uses `contextlib.AsyncExitStack()` for proper resource management when no client provided
- The `stream()` function combines chunked reading with `StreamFromIter` to create a standard Python file object
- Tests use botocore stubbing for mocking S3 operations

### Dependencies

- **aiobotocore** - Async boto3 client for S3 operations
- **multidict** - Required dependency for aiobotocore

### Testing Structure

Tests are in `tests/test_aios3_file.py` and use:
- `pytest-asyncio` for async test support
- `botocore.stub.Stubber` for mocking S3 operations
- Custom `Stream` class in tests to simulate S3 response objects
- Fixtures defined in `tests/conftest.py`

## Build System

- Uses **hatchling** as build backend
- Project metadata in `pyproject.toml`
- Version managed in `src/aios3/__about__.py`
- Supports Python 3.10+

## Pre-commit Configuration

The project uses extensive pre-commit hooks:
- **ruff** - Fast Python linter and formatter (with --fix)
- **mypy** - Type checking with strict settings
- **pylint** - Additional linting with max line length 99

Excludes: tests/, site/, docs/, setup.py, version.py