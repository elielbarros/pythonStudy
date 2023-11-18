"""
TUPLE

Tuple does not support item assignment

If I want a list that it is not possible to remove or edit it is possible to use a tuple

Tuple could be used with parentheses or without
"""

names = "John", "Mary", "David"
print(names, type(names))
print(names[0])

# It is possible to create a tuple by list
list_a = ["John", "Mary", "David"]
tuple_a = tuple(list_a)
print(tuple_a, type(tuple_a), list_a, type(list_a))

# It is possible to create a list by tuple
tuple_b = ("John", "Mary", "David")
list_b = list(tuple_b)
print(list_b, type(list_b))

tuple_ = ()
print(type(tuple_))  # output: <class 'tuple'>
