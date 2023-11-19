"""
List - Mapping
"""

# Mapping data with list comprehension
products = [
    {'name': 'product1', 'price': 20},
    {'name': 'product2', 'price': 10},
    {'name': 'product3', 'price': 30},
]

new_products = [
    product
    for product in products
]
print(*new_products, sep='\n')
# output:
# {'name': 'product1', 'price': 20}
# {'name': 'product2', 'price': 10}
# {'name': 'product3', 'price': 30}

# We can also map just one value from the list products
new_products = [
    {'name': product['name']}
    for product in products
]
print(*new_products, sep='\n')
# output:
# {'name': 'product1'}
# {'name': 'product2'}
# {'name': 'product3'}

# We can also map the price of each product multiplying each price by 1.5
new_products = [
    {**product, 'price': product['price'] * 1.5}
    for product in products
]
print(*new_products, sep='\n')
# output:
# {'name': 'product1', 'price': 30.0}
# {'name': 'product2', 'price': 15.0}
# {'name': 'product3', 'price': 45.0}

# We can also map the price using a condition
# On this case, 1.5 will multiply only value greater than 16
new_products = [
    {**product, 'price': product['price'] * 1.5}
    if product['price'] > 16 else {**product}
    for product in products
]
print(*new_products, sep='\n')
# output:
# {'name': 'product1', 'price': 30.0}
# {'name': 'product2', 'price': 10}
# {'name': 'product3', 'price': 45.0}

