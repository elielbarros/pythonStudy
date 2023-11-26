"""
# English
itertools - zip_longest

zip_longest(list_a, list_b) will join list_a into list_b considering list with max length

zip_longest(list_a, list_b, fillvalue='something here') the param 'fillvalue' will fill non-existent value to the minor
list with 'something here'

zip_longest return iterator, so we can iterate over a zip_longest object with 'for' to access values

# Portuguese
Class zip

zip_longest(list_a, list_b) vai juntar list_a e list_b considerando a lista de maior tamanho

zip_longest(list_a, list_b, fillvalue='something here') vai preencher os valores inexistentes para a lista de menor
tamanho com 'something here'

zip_longest retorna iterator, entao podemos iterar sobre o objeto zip_longest utilizando 'for' para acessar os valores
"""
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(*list(zip_longest(l1, l2, fillvalue='Without value')), sep='\n')
# output:
# ('Salvador', 'BA')
# ('Ubatuba', 'SP')
# ('Belo Horizonte', 'MG')
# ('Without value', 'RJ')
