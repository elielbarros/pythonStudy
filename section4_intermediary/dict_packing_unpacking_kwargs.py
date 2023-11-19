# UNPACK
person = {
    'name': 'John',
    'last_name': 'Doe'
}

# To UNPACK dictionary keys into variables, do:
name_key, last_name_key = person
print(f'{name_key=}', f'{last_name_key=}')  # output: name='name' last_name='last_name'

# To UNPACK dictionary values into variables, do:
name_value, last_name_value = person.values()
print(f'{name_value=}', f'{last_name_value=}')  # output: name_value='John' last_name_value='Doe'

# We can UNPACK dictionary as a tuple with key and value
name_key_value, last_name_key_value = person.items()
print(f'{name_key_value=}',
      f'{last_name_key_value=}')  # output: name_key_value=('name', 'John') last_name_key_value=('last_name', 'Doe')

# We can UNPACK dictionary from a tuple key and value into two different variables
(name_key, name_value), last_name_key_value = person.items()
print(f'{name_key=}', f'{name_value=}',
      f'{last_name_key_value=}')  # output: name_key='name' name_value='John' last_name_key_value=('last_name', 'Doe')

# We can also UNPACK the dictionary iterating over it
for key, value in person.items():
    print(key, value)
    # output:
    # name John
    # last_name Doe

# PACK
# It is possible to PACK a dictionary inside another one
another_person = {**person}
print(another_person)  # output: {'name': 'John', 'last_name': 'Doe'}

# It is also possible to PACK and edit the value that is get in on another dictionary
another_person = {**person, 'name': 'Alice'}
print(another_person)  # output: {'name': 'Alice', 'last_name': 'Doe'}

# It is also possible to PACK and include another information too
another_person = {**person, 'name': 'Alice', 'age': 100}
print(another_person)  # output: {'name': 'Alice', 'last_name': 'Doe', 'age': 100}

# It is also possible to PACK more than one dictionary inside another
person_information = {
    'age': 100,
    'height': 1.80
}

another_person = {**person, **person_information}
print(another_person)  # output: {'name': 'John', 'last_name': 'Doe', 'age': 100, 'height': 1.8}


# KWARGS
def print_named_args(*args, **kwargs):
    print('NOT NAMED ARGS (ARGS):', args)  # output: NOT NAMED ARGS (ARGS):  ()
    print('NAMED ARGS (KWARGS):', kwargs)  # output: NAMED ARGS (KWARGS): {'name': 'Max', 'last_name': 'Meyers'}
    for key, value in kwargs.items():
        print(key, value)
        # output:
        # name Max
        # last_name Meyers


# We can pass named args for method, and this params will be included in param as dictionary
print_named_args(name='Max', last_name='Meyers')

# It is also possible to send packed dict as kwargs
print_named_args(**person)
# outputs:
# NOT NAMED ARGS (ARGS): ()
# NAMED ARGS (KWARGS): {'name': 'John', 'last_name': 'Doe'}
# name John
# last_name Doe
