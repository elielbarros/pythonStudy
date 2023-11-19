"""
Fast way to create a list using iterable.
"""

list_ = list(range(5))
print(list_)  # output: [0, 1, 2, 3, 4]

# As we known .range() is a method that returns iterable of values.
# We can do something like this
list_ = [number for number in range(5)]
print(list_)  # output: [0, 1, 2, 3, 4]

# We can also multiply the number by 2
list_ = [number * 2 for number in range(5)]
print(list_)  # output: [0, 2, 4, 6, 8]
