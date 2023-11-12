"""
Type list
1. list is mutable
2. support many types and values
3. reusable
4. principal methods: append, insert, pop, del, clear, extend, +
"""

example_string = 'ABCDE'
example_list = []
# If list is empty, bool returns False
print(example_list, type(example_list), bool(example_list), sep=' || ')

example_2_list = [123, True, 'Hello World', 1.2, []]

print(example_2_list)

for element in example_2_list:
    print(element, type(element), bool(element), sep=' || ')


# It's possible to change one specific value on list
example_2_list[1] = False
print(example_2_list[1])



