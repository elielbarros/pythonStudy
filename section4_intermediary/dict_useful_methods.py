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
"""

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
