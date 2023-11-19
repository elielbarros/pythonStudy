"""
'.sort()' method will serve to order a list

The method could also order a dict and to do that, we have to say the key from dict that we want to order
"""

list_ = [1, 3, 7, 5, 2, 8, 0]
list_.sort()
print(list_)  # output: [0, 1, 2, 3, 5, 7, 8]

# Ordering a list of dictionaries
list_ = [
    {'name': 'Andrew', 'last_name': 'Hamilton'},
    {'name': 'Layla', 'last_name': 'Boyle'},
    {'name': 'Tiago', 'last_name': 'Glover'},
    {'name': 'Adnan', 'last_name': 'Hopkins'},
]


# To order a dictionary array, we can use sort, passing the key that we want to consider ordering
def order_by_name(item):
    print(item)
    return item['name']


list_.sort(key=order_by_name)
print()
print()
for element in list_:
    print(element)

# output
# {'name': 'Adnan', 'last_name': 'Hopkins'}
# {'name': 'Andrew', 'last_name': 'Hamilton'}
# {'name': 'Layla', 'last_name': 'Boyle'}
# {'name': 'Tiago', 'last_name': 'Glover'}