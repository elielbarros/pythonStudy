"""
Key-Word used to create anonymous functions.

Anonymous Function is a function that was not defined. Does not have a formal name.

Basic syntax:
lambda argument: expression
"""
# Example 1
sum_ = lambda x, y: x + y
print(sum_(3, 5))  # Output: 8

# Example 2
list_ = [
    {'name': 'Andrew', 'last_name': 'Hamilton'},
    {'name': 'Layla', 'last_name': 'Boyle'},
    {'name': 'Tiago', 'last_name': 'Glover'},
    {'name': 'Adnan', 'last_name': 'Hopkins'},
]

list_.sort(key=lambda item: item['name'])
for element in list_:
    print(element)
