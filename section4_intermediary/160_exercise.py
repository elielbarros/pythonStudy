import copy

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]
print(*products, sep='\n')

print()

# Apply 10% more in each product price
# Generate new products using deep copy
new_products = [
    {**product, 'price': round(product['price'] * 1.1, 2)}
    for product in copy.deepcopy(products)
]
print(*new_products, sep='\n')

print()

# Order products by name DESC
# Generate new products_ordered_by_name using deep copy
products_ordered_by_name = copy.deepcopy(products)
products_ordered_by_name.sort(key=lambda product: product['name'])
products_ordered_by_name.reverse()
print(*products_ordered_by_name, sep='\n')

print()

# Using sorted()
print('products ordered by name using sorted()')
products_ordered_by_name = sorted(copy.deepcopy(products), key=lambda product: product['name'], reverse=True)
print(*products_ordered_by_name, sep='\n')

print()

# Order products by price ASC
# Generate new products_ordered_by_price using deep copy
products_ordered_by_price = copy.deepcopy(products)
products_ordered_by_price.sort(key=lambda product: product['price'])
print(*products_ordered_by_price, sep='\n')

print()

# Using sorted()
print('products ordered by price using sorted()')
products_ordered_by_price = sorted(copy.deepcopy(products), key=lambda product: product['price'])
print(*products_ordered_by_price, sep='\n')


