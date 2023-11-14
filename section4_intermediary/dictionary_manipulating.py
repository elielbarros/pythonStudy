"""
Manipulating 'key' and 'value' with dictionary
"""

# Creating a dictionary
person = {}

# Creating a key for dictionary
key_ = 'name'

# Giving for the key a value
person[key_] = 'John'

print(person, person[key_])

# Creating another key with value already
person['last_name'] = 'Doe'
print(person, person['last_name'])

# Deleting 'key' and respective 'value' from dict
del person['last_name']
print(person)

# If you try to print a dict using a nonexistent 'key', it will raise an error
# print(person['any_key'])  # KeyError: 'any_key'
# If you want to try to get a key, even this key does not exist
if not person.get('any_key'):
    print('This key does not exist')
else:
    print(person.get('any_key'))
