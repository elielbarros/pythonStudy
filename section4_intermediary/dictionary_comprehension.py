"""
Dictionary - Comprehension
"""

product = {
    'name': 'Pencil',
    'price': 2.50,
    'category': 'Office'
}

print(*product.items(), sep='\n')
# output:
# ('name', 'Pencil')
# ('price', 2.5)
# ('category', 'Office')

print()

# Using comprehension to create a new dictionary iterating over last dictionary created
new_product = {
    key: value
    for key, value in product.items()
}

print(*new_product.items(), sep='\n')
# output:
# ('name', 'Pencil')
# ('price', 2.5)
# ('category', 'Office')

print()

# It is possible to MAP 'value' information using a condition
new_product = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
}

print(*new_product.items(), sep='\n')
# output:
# ('name', 'PENCIL')
# ('price', 2.5)
# ('category', 'OFFICE')

print()

# It is possible to FILTER dictionary and get just one element by the key
new_product = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key == 'category'
}

print(*new_product.items(), sep='\n')
# output:
# ('category', 'OFFICE')

print()

# It is possible to create a dictionary from a list too
list_ = [
    ('key_a', 'value_a'),
    ('key_b', 'value_b'),
    ('key_c', 'value_c')
]

new_dictionary = {
    key: value
    for key, value in list_
}
print(*new_dictionary.items(), sep='\n')
# output:
# ('key_a', 'value_a')
# ('key_b', 'value_b')
# ('key_c', 'value_c')

print()

# But we can do the same made before just using list as param on dict() constructor
new_dictionary = dict(list_)
print(*new_dictionary.items(), sep='\n')
# output:
# ('key_a', 'value_a')
# ('key_b', 'value_b')
# ('key_c', 'value_c')
