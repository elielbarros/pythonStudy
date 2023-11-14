"""
Dictionary on Python

Dictionary Struct is composed by 'Key' and 'Value'.

'Key' could be an Index.
'Key' could be immutable types as: str, int, float, bool, tuple, etc.

Value could be anything, including another dictionary.

To create a dictionary, we can use '{}' or the dictionary class to create dictionaries.

Immutable: str, int, float, bool, tuple
Mutable: dict, list

person = {
    'name': 'John',
    'last_name': 'Doe',
    'age': 18,
    'height': 1.80,
    'address': [
        {'street': 'example street', 'number': 123},
        {'street': 'another example street', 'number': 321},
    ]
}

print(person, type(person))
"""
person = dict(name='John', last_name='Doe', age=18, height=1.80,
              address=[dict(street='example street', number=123), dict(street='another example street', number=321)])
print(person, type(person))
print(person['name'])
print(person['address'][0]['street'])

person = {
    'name': 'John',
    'last_name': 'Doe',
    'age': 18,
    'height': 1.80,
    'address': [
        {'street': 'example street', 'number': 123},
        {'street': 'another example street', 'number': 321},
    ]
}

print(person, type(person))

for key in person:
    print(key, person[key])
