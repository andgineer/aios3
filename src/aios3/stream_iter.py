"""Create file-like object from iterable/iterator."""

import io
from array import array
from typing import Iterable, Iterator, Optional, Union


class StreamFromIter(io.RawIOBase):
    """Stream bytes from iterable/iterator.

    >>> def chunks():
    ...     for chunk in [b"foo", b"bar", b"spam"]:
    ...         yield chunk
    >>> with io.BufferedReader(StreamFromIter(chunks())) as stream:
    ...     print(stream.read())
    b'foobarspam'
    >>> with StreamFromIter([b"foo", b"bar", b"spam"]) as stream:
    ...     print(stream.read())
    b'foobarspam'
    """

    def __init__(
        self,
        source: Union[  # type: ignore
            Iterator[Union[bytearray, array]],
            Iterable[Union[bytearray, array]],
        ],
    ):
        """Implement Python io stream protocol.

        Args:
            source: iterable or iterator that produce bytes.
        """
        self.leftover: Optional[Union[bytearray, array]] = None  # type: ignore
        self.iterator = source if isinstance(source, Iterator) else iter(source)
        super().__init__()

    def readable(self) -> bool:
        """Implement abstract method in io.IOBase.

        Return:
             const True to confirm the stream can be read from.
        """
        return True

    def readinto(self, allocated_buffer: Union[bytearray, array]) -> int:  # type: ignore
        """Implement abstract method in io.RawIOBase.

        Read bytes into a pre-allocated, writable bytes-like object b,
        and return the number of bytes read.
        For example, b might be a bytearray.
        If the object is in non-blocking mode and no bytes are available, None is returned.

        Args:
            allocated_buffer: buffer to read into.

        Return:
            Number of read bytes.
        """
        try:
            max_bytes_in_result = len(allocated_buffer)
            chunk = self.leftover or next(self.iterator)
            output, self.leftover = (
                chunk[:max_bytes_in_result],
                chunk[max_bytes_in_result:],
            )
            allocated_buffer[: len(output)] = output  # type: ignore
            return len(output)
        except StopIteration:
            return 0  # indicate EOF


if __name__ == "__main__":
    import doctest

    doctest.testmod()
