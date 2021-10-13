<!-- markdownlint-disable -->

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/stream_iter.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `stream_iter`
Create file-like object from iterable/iterator.



---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/stream_iter.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `StreamFromIter`
Stream bytes from iterable/iterator.

``` def chunks():```
...     for chunk in [b"foo", b"bar", b"spam"]:
...         yield chunk
``` with io.BufferedReader(StreamFromIter(chunks())) as stream:``` ...     print(stream.read()) b'foobarspam' ``` with StreamFromIter([b"foo", b"bar", b"spam"]) as stream:```
...     print(stream.read())
b'foobarspam'


<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/stream_iter.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    source: Union[Iterator[Union[bytearray, array]], Iterable[Union[bytearray, array]]]
)
```

Implement Python io stream protocol.



**Args:**

 - <b>`source`</b>:  iterable or iterator that produce bytes.




---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/stream_iter.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `readable`

```python
readable() → bool
```

Implement abstract method in io.IOBase.

Return:  const True to confirm the stream can be read from.

---

<a href="https://github.com/andgineer/aios3/blob/master/src/aios3/stream_iter.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `readinto`

```python
readinto(allocated_buffer: Union[bytearray, array]) → int
```

Implement abstract method in io.RawIOBase.

Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read. For example, b might be a bytearray. If the object is in non-blocking mode and no bytes are available, None is returned.



**Args:**

 - <b>`allocated_buffer`</b>:  buffer to read into.

Return: Number of read bytes.




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
