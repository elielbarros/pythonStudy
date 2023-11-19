"""
List - Filter
"""

products = [
    {'name': 'product1', 'price': 20},
    {'name': 'product2', 'price': 10},
    {'name': 'product3', 'price': 30},
]

# To filter a list with dictionary, we can use if after for iterate.
# Here we are considering the products that have the price less than 20.
# It is important to understand that the filtering is working without a
# considered map 'if product['price'] > 16 else {**product}'.
# So the filter is seeing the product price itself without multiplying by 1.5
new_products = [
    {**product, 'price': product['price'] * 1.5}
    if product['price'] > 16 else {**product}
    for product in products
    if product['price'] < 20
]
print(*new_products, sep='\n') # output: {'name': 'product2', 'price': 10}


