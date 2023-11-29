"""
# English
filter - Will filter a list considering a filter
Example: filter(method, list)
This method could be lambda and could be a defined method

# Portuguese
filter - Vai filtrar uma lista considerando um filtro
Exemplo: filter(method, list)
Esse metodo pode ser lambda e pode ser um metodo definido
"""

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

new_products_comprehension_filter = [
    product for product in products
    if product['price'] > 10
]

print(*new_products_comprehension_filter, sep='\n')
# output:
# {'name': 'Product 1', 'price': 22.32}
# {'name': 'Product 3', 'price': 10.11}
# {'name': 'Product 2', 'price': 105.87}
# {'name': 'Product 4', 'price': 69.9}

print()

new_products_filter = filter(
        lambda product: product['price'] > 10,
        products
)
print(*new_products_filter, sep='\n')
# output:
# {'name': 'Product 1', 'price': 22.32}
# {'name': 'Product 3', 'price': 10.11}
# {'name': 'Product 2', 'price': 105.87}
# {'name': 'Product 4', 'price': 69.9}

print()


def product_condition_filter(product):
    return product['price'] > 50


new_products_filter_using_defined_method = filter(
        product_condition_filter,
        products
)

print(*new_products_filter_using_defined_method, sep='\n')
# output:
# {'name': 'Product 2', 'price': 105.87}
# {'name': 'Product 4', 'price': 69.9}
