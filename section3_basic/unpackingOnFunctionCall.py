"""
Unpacking function call
"""

# It is possible to get the first element and last element and everything between first and last element
list_ex = ['Hello', 'World', '!', 'John', 'Doe']
first_element, *between_element, last_element = list_ex
print(first_element, last_element)

# It is possible to print the list already unpacked.
# It will look like we are getting item by item using some iterator as for ou while
print(list_ex)
print('Unpacked list:', *list_ex)

# We could also unpack lists inside list. For example:
rooms = [
    ['chair_1', 'chair_2'],
    ['chair_3', 'chair_4'],
    ['chair_5', 'chair_6']
]
print(*rooms, sep='\n')  # To be more beautiful, we are using sep with 'line break'
