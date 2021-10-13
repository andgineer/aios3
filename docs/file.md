<!-- markdownlint-disable -->

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `file`
S3 "files" operations with aiobotocore.


---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/file.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `save`

```python
save(
    bucket: str,
    key: str,
    body: bytes,
    s3: Optional[AioBaseClient] = None
) → None
```

Create the file with the `body`.



**Args:**

 - <b>`bucket`</b>:  S3 bucket.
 - <b>`key`</b>:  path in the bucket including "file name".
 - <b>`body`</b>:  content to write into file.
 - <b>`s3`</b>:  boto s3 client. by default it auto-created inside the function.


---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/file.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read`

```python
read(bucket: str, key: str, s3: Optional[AioBaseClient] = None) → bytes
```

Read the full content of the file as bytes.



**Args:**

 - <b>`bucket`</b>:  S3 bucket.
 - <b>`key`</b>:  path in the bucket including "file name".
 - <b>`s3`</b>:  boto s3 client. by default it auto-created inside the function.

Return: The file content as bytes.


---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/file.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `chunks`

```python
chunks(
    bucket: str,
    key: str,
    s3: Optional[AioBaseClient] = None
) → AsyncGenerator[bytearray, NoneType]
```

Generate file chunks as they are returned by AWS.



**Args:**

 - <b>`bucket`</b>:  S3 bucket.
 - <b>`key`</b>:  path in the bucket including "file name".
 - <b>`s3`</b>:  boto s3 client. by default it auto-created inside the function.

Return: Chunks of the file.


---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/file.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `stream`

```python
stream(bucket: str, key: str, s3: Optional[AioBaseClient] = None) → IO[bytes]
```

Create file-like object to stream the file content.



**Args:**

 - <b>`bucket`</b>:  S3 bucket.
 - <b>`key`</b>:  path in the bucket including "file name".
 - <b>`s3`</b>:  boto s3 client. by default it auto-created inside the function.

Return: Python file stream with the file content.




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
