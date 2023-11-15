"""
Dict - Useful Methods

len - Will return how many keys have dict
keys - Will return iterable for keys
values - Will return iterable for values
items - Will return iterable for keys and values
setdefault - add value if key does not exist
copy - return 'shallow copy'
get - get value from key
pop - delete an item with specific key (del)
popitem - Delete last item added
update - update dict with another
deep copy - will copy everything from dict_a to dict_b as a new dict.
"""

import copy

person = {
    'name': 'John',
    'last_name': 'Doe 1',  # Create key and value
    'last_name': 'Doe 2',  # Update key and value
    'last_name': 'Doe'  # Update key and value again. It will return only this last name
}

print(f'{person.__len__()=}')
print(f'{person["last_name"]}')

# I can convert iterable on tuple or list
print(tuple(person.keys()))
print(list(person.keys()))
# It is possible to iterate over keys with for
for key_ in person.keys():
    print(f'{key_=}')

# same for values
print(tuple(person.values()))
print(list(person.values()))
# It is possible to iterate over values with for
for values in person.values():
    print(f'{values=}')

# It is possible to get items as iterable:
print(person.items())
print(tuple(person.items()))
print(list(person.items()))
# Using the method items() that return key and value as tuple, it is possible to unpack this information
for key_, value in person.items():
    print(key_, value)

# If the dict does not have a specific key, it is possible that this key will come sometime;
# we could try to use setdefault(), so when this key in specific didn't come, it is just set a default value for it
person = {
    'name': 'John',
    'last_name': 'Doe'
}

person.setdefault('age', '0')
print(f'{person.get("age")=}')

# It is possible to copy a dict into another dict pointing dict_2 to dict_1
dict_1 = {
    'c1': 1
}

dict_2 = dict_1
print(dict_2)  # output: {'c1': 1}

# But if change dict_2, then dict_1 will be changed too
dict_2['c1'] = 100
print(dict_1)  # output: {'c1': 100}

# So we can make a 'Shallow Copy'.
# 'Shallow Copy' will definitely copy immutable values.
# But mutable values will be pointed as before when we pointed dict_2 to dict_1.
dict_1 = {
    'c1': 1,
    'l1': [1, 2, 3]
}
dict_2 = dict_1.copy()
dict_2['c1'] = 100
print(dict_2)  # output: {'c1': 100, 'l1': [1, 2, 3]}
dict_2['l1'][0] = 100
print(dict_1)  # output: {'c1': 1, 'l1': [100, 2, 3]}

# It is possible to make a 'Shallow Copy' with library copy
dict_2 = copy.copy(dict_1)
print(dict_2)  # output: {'c1': 1, 'l1': [100, 2, 3]}

# It is possible to make a 'Deep Copy' with library copy
# 'Deep Copy' will copy all information from dict_a to dict_b as a new dict in memory.
dict_a = {
    'a': 1,
    'la': [1, 2, 3]
}
dict_b = copy.deepcopy(dict_a)
dict_b['a'] = 100
dict_b['la'][1] = 100
print(dict_a)  # output: {'a': 1, 'la': [1, 2, 3]}
print(dict_b)  # output: {'a': 100, 'la': [1, 100, 3]}

# It is possible to pop an item from dict
pop_ = {
    'a': 1,
    'b': 2
}
print(pop_)  # output: {'a': 1, 'b': 2}
pop_a = pop_.pop('a')
print(pop_a)  # output: 1
print(pop_)  # output: {'b': 2}
pop_item = pop_.popitem()
print(pop_item)  # output: ('b', 2)
print(pop_)  # {}


# It is also possible to update a dict with method update()
update_ = {
    'a': 1
}
print(update_)
