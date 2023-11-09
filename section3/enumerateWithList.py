"""
Enumerate

Enumerate will iterate over list with index

It is possible to start the index of the enumerate method. enumerate(list_example, start=10)
"""

list_a = ['Hello', 'World', '!']

enumerated_list = enumerate(list_a)
print(enumerated_list)

# It is possible to get the first value with next method
# With enumerate it will be generated a tuple with index value and value | (0, 'Hello')
print(next(enumerated_list), type(next(enumerated_list)))

for item in enumerated_list:
    print(item)

# It is possible to see that enumerate when in a variable after consumed with an iterable it won't be possible to
# iterate again... to do that is necessary tu use the method over the method again
for item in enumerate(list_a):
    print(item)

# It is possible to convert the list enumerated in another list with tuple
# Because of that I can consume this list how many times i want
list_from_enumerated_list = list(enumerate(list_a))
print(list_from_enumerated_list)

# It is possible to iterate over enumerated list getting the index and the value separated in two different values
# It is the UNPACKING
for index, word in enumerate(list_a):
    print(index, word)

# Just another way
for item in enumerate(list_a):
    index, word = item
    print(index, word)
