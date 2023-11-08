"""
When we point list B to list A, we are pointing for the list with the values Hello and World.
If we change on list A value Hello, the list B will be changed together and vice versa.

It is important to understand it. We are changing the values from the same list we are pointing with list_a and list_b.

So... We are pointing with list_a and list_b for the list ['Hello', 'World'] already in memory.

If we want to have two different lists with the same value but not changing it when change the lists, we have to copy it
The example is with list c and list b
"""

list_a = ['Hello', 'World']
list_b = list_a

list_a[0] = 'Hi'
print(list_b)

list_b[1] = 'John'
print(list_a)

list_c = ['Home', 'work']
list_d = list_c.copy()

list_c[0] = 'my'
print(list_d)

list_d[1] = 'base'
print(list_c)
print(list_d)

