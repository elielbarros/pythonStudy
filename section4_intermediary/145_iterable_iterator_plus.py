"""
Iterable: Object that can be walked through (list, tuple, string, dictionary, set, etc.)

Iterator: Will maintain the object state during iteration and knows how to get the next value when claimed
"""

iterable = ['I', 'have', '__iter__']
iterator = iterable.__iter__()  # <list_iterator object at 0x7f156c587c10>

# print(iterator[0])  # TypeError: 'list_iterator' object is not subscriptable
# print(len(iterator))  # TypeError: object of type 'list_iterator' has no len()

print(next(iterator))  # output: I

iterator_ = iter(iterable)
print(next(iterator_))  # output: I
print(next(iterator_))  # output: have
print(next(iterator_))  # output: __iter__
# print(next(iterator_))  # output: StopIteration

