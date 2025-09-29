# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

aios3 is a Python library that provides file-like objects for reading AWS S3 files by chunks using aiobotocore. The main functionality is creating streamable interfaces to S3 objects for asynchronous operations.

## Development Environment Setup

The project uses UV for dependency management and virtual environment handling:

```bash
# Source the activation script to set up or activate the development environment
source ./activate.sh
```

**IMPORTANT**: Always activate the virtual environment before running any commands. Use `source ./activate.sh` before each command.

This script:
- Creates a virtual environment using Python 3.11 if it doesn't exist
- Activates the virtual environment
- Installs dependencies with `uv sync --frozen`

## Common Development Commands

### Testing
```bash
# Run all tests with pytest (use python -m pytest for proper module loading)
source ./activate.sh && python -m pytest -v

# Run tests with coverage
source ./activate.sh && python -m pytest --cov

# Run specific test file
source ./activate.sh && python -m pytest tests/test_aios3_file.py -v

# Tests include doctests (configured in pytest.ini)
```

### Code Quality
```bash
# Run pre-commit hooks (includes ruff, mypy, pylint)
source ./activate.sh && pre-commit run --all-files
```

**IMPORTANT**: Always use `pre-commit run --all-files` for code quality checks. Never run ruff, mypy, or pylint directly.

### Documentation
```bash
# Build and serve English documentation
source ./activate.sh && make docs

# Build and serve Russian documentation
source ./activate.sh && make docs-ru
```

### Version Management
```bash
# Bump version for bug fix
source ./activate.sh && make ver-bug

# Bump version for feature
source ./activate.sh && make ver-feature

# Bump version for release
source ./activate.sh && make ver-release
```

### Dependency Management
```bash
# Upgrade all dependencies including pre-commit hooks
source ./activate.sh && make reqs
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
