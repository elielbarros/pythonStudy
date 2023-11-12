"""
Type list
1. list is mutable
2. support many types and values
3. reusable
4. principal methods: append, insert, pop, del, clear, extend, +
"""

ex_list = [1, 2, 3, 4]
print(ex_list)

# It's possible to get the element from the list and use in another variable
value = ex_list[2]
print(value)

# It's possible to change a specific element from list
ex_list[2] = 5
print(ex_list[2])

# It's possible to DELETE one element from list
# To do that Python moves next elements to the index before
del ex_list[3]
print(ex_list)

# It's possible to add an element into the final of the list
ex_list.append(6)
print(ex_list)

# It's possible to delete the last element from the list
# The method pop return the element removed
removed = ex_list.pop()
print(removed)
print(ex_list)

# It's possible to delete an element by index with pop too
removed = ex_list.pop(1)
print(removed)
print(ex_list)

# It's possible to insert an element in a specific index
# It's not possible to access index after the last list index
# It's only possible to insert an element between the initial and last index available
ex_list.insert(1, 2)
print(ex_list)





