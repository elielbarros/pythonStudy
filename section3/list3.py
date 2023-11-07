"""
Type list
1. list is mutable
2. support many types and values
3. reusable
4. principal methods: append, insert, pop, del, clear, extend, +
"""

# It's possible to CONCATENATE two lists and put the result inside another list C
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c)

# It's possible to put the values from list b inside list a
list_a.extend(list_b)
print(list_a)
