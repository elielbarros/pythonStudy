"""
https://docs.python.org/3/library/collections.abc.html
"""

from collections.abc import Iterable


class MyList(Iterable):
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __iter__(self):
        ...


list_ = MyList()
list_.append('John')
list_.append('Mary')
print(list_._data)
