# aioS3

[aiobotocore](https://aiobotocore.readthedocs.io/en/latest/) read large files in chunks.
So to read total file you have to create loop like that

```python
resp = yield from s3.get_object(Bucket='mybucket', Key='k')
stream = resp['Body']
try:
    chunk = yield from stream.read(10)
    while len(chunk) > 0:
      ...
      chunk = yield from stream.read(10)
finally:
  stream.close()
```

This is kind of laborious if you do not want to use this chunks somehow (like process them chunk by chunk and
get all advantages from async operations).

In most cases you just want this file read.

And aioS3 does exactly that - it wrap aiobotcore operations with simple functions like
[read()](api-reference/file.html/#function-read) that return
full file content.

But it can do more - there is [stream()](api-reference/file.html/#function-stream)
where you have simple file-like interface and in some cases can be more
effective, if you do not read file as one piece.

# Documentation

[aioS3 API reference](api-reference/)
