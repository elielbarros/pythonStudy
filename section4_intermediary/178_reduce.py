"""
# English
reduce - reduces values into a single value
reduce must be imported from functools
reduce is a method with condition, a list to be evaluated and 'previous' value or initial value
reduce(method, list, previous_value)

# Portuguese
reduce - reduz valores em um unico valor
reduce precisa ser importado de functools
reduce eh um metodo com codicao, uma lista a ser avaliada e um valor 'anterior' ou valor inicial
reduce(metodo, lista, valor_anterior)
"""
from functools import reduce

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]


def biggest_product_price_condition(previous, product):
    return previous if previous['price'] > product['price'] else product


# Using defined method to reduce
biggest_product_price = reduce(
        biggest_product_price_condition,
        products,
        products[0]
)

print(biggest_product_price)

print()

# Using lambda to reduce
smallest_product_price = reduce(
        lambda previous, product: previous if previous['price'] < product['price'] else product,
        products,
        products[0]
)

print(smallest_product_price)
