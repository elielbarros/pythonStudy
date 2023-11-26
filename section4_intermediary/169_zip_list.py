"""
# English
Class zip

zip(list_a, list_b) will join list_a into list_b considering list with minor length

zip return iterator, so we can iterate over a zip object with 'for' to access values

# Portuguese
Class zip

zip(list_a, list_b) vai juntar list_a e list_b considerando a lista de menor tamanho

zip retorna iterator, entao podemos iterar sobre o objeto zip utilizando 'for' para acessar os valores
"""

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(*list(zip(l1, l2)), sep='\n')
# output:
# ('Salvador', 'BA')
# ('Ubatuba', 'SP')
# ('Belo Horizonte', 'MG')
