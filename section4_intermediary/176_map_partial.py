"""
# English
map - will map data
partial - work as a closure function

# Portuguese
map - Serve para mapear dados
partial - funciona como uma 'closure function'
"""
from functools import partial
from types import GeneratorType

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]


def apply_percentage(value, percentage):
    return round(value * percentage, 2)


apply_ten_per_cent = partial(
        apply_percentage,
        percentage=1.1
)

new_product = [
    {**product, 'price': apply_ten_per_cent(product['price'])}
    for product in products
]

# Here we have new product as a list
print(type(new_product))  # output: <class 'list'>
print(*new_product, sep='\n')
# output:
# {'name': 'Product 5', 'price': 11.0}
# {'name': 'Product 1', 'price': 24.55}
# {'name': 'Product 3', 'price': 11.12}
# {'name': 'Product 2', 'price': 116.46}
# {'name': 'Product 4', 'price': 76.89}

print()


def change_product_price(product):
    return {**product, 'price': apply_ten_per_cent(product['price'])}


# It is possible to map a product as list comprehension with map() method
# map will could receive a method to apply a map and the list to map
# It is important to understand that map as generator are exhaustible, has an end.
# If we iterate over new product mapped, we will get on an end.
# If we always want to have access to map values, we have to convert it using list
# For example list(map())
new_product_mapped = map(change_product_price, products)

print(*new_product_mapped, sep='\n')
# output:
# {'name': 'Product 5', 'price': 11.0}
# {'name': 'Product 1', 'price': 24.55}
# {'name': 'Product 3', 'price': 11.12}
# {'name': 'Product 2', 'price': 116.46}
# {'name': 'Product 4', 'price': 76.89}
print(new_product_mapped)  # output: <map object at 0x7f195928fd30>
print(hasattr(new_product_mapped, '__iter__'))  # output: True
print(hasattr(new_product_mapped, '__next__'))  # output: True

# Here we have a generator object, that is different of a map object
# But has iter and next because it is iterable
new_product_generator = (product for product in products)
print(new_product_generator)  # output: <generator object <genexpr> at 0x7f19593f4110>
print(hasattr(new_product_generator, '__iter__'))  # output: True
print(hasattr(new_product_generator, '__next__'))  # output: True
print(isinstance(new_product_generator, GeneratorType))  # output: True

print(
        *map(lambda x: x * 2, [1, 2, 3, 4]), sep='\n'
)
# output:
# 2
# 4
# 6
# 8
