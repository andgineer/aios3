# aioS3

[aiobotocore](https://aiobotocore.readthedocs.io/en/latest/) can read large files in chunks.

To read total file you have to create loop like that

```python
resp = yield from s3.get_object(Bucket='mybucket', Key='k')
stream = resp['Body']
try:
    while True:
      chunk = yield from stream.read(1024)
      ...
      if len(chunk) > 0:
          break
finally:
  stream.close()
```

But if you need file-like object for something like `pickle.load()` or `json.load()` you cannot read by chunks -
it will read full file.
In some cases it can be ineffective - for example `pickle` read objects piece by piece, you do not need to
load full file in memory for that.

With aioS3 [stream()](docstrings/file/#function-stream) you have file-like interface with customizable chunk size.

# Documentation

[aioS3 API reference](docstrings/)

# source code

[andgineer/aios3](https://github.com/andgineer/aios3)
