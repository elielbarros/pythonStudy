"""
.isinstance(object, type)

It will check if an object is an instance of type
"""

list_ = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'name', 'John'}
]

for object_ in list_:
    print(object_, isinstance(object_, set))
# output:
# a False
# 1 False
# 1.1 False
# True False
# [0, 1, 2] False
# (1, 2) False
# {0, 1} True
# {'name', 'John'} True

print()

# We can check two types at the same time with .isinstance()
number = 1.1
if isinstance(number, (int, float)):
    print(number, number * 2)  # output: 1.1 | 2.2
