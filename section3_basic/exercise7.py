"""
It is possible to get size from list with len()
"""
list_a = ['Hello', 'World', '!']

indexes = range(len(list_a))

for index in indexes:
    print(index, list_a[index], type(list_a[index]))
