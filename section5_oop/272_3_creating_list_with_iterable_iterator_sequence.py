"""
https://docs.python.org/3/library/collections.abc.html
"""

from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return self._index

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value



list_ = MyList()
list_.append('John')
list_.append('Mary', 'Jane')

print(list_[1])  # output: Mary
print(len(list_))  # output: 2

for item in list_:
    print(item)

list_[0] = 'Another'
print(list_[0])  # output: Another

for item in list_:
    print(item)
