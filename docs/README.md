<!-- markdownlint-disable -->

# API Overview

## Modules

- [`file`](./file.md#module-file): S3 "files" operations with aiobotocore.
- [`stream_iter`](./stream_iter.md#module-stream_iter): Create file-like object from iterable/iterator.
- [`version`](./version.md#module-version)

## Classes

- [`stream_iter.StreamFromIter`](./stream_iter.md#class-streamfromiter): Stream bytes from iterable/iterator.

## Functions

- [`file.chunks`](./file.md#function-chunks): Generate file chunks as they are returned by AWS.
- [`file.read`](./file.md#function-read): Read the full content of the file as bytes.
- [`file.save`](./file.md#function-save): Create the file with the `body`.
- [`file.stream`](./file.md#function-stream): Create file-like object to stream the file content.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
