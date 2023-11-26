"""
# English
Considering two integer/float lists (list_a and list_b)
Sum list_a[i] with list_b[i] returning a new list with sum values:
If one list are biggest than another, the sum will consider only smallest list size.
Example:
list_a     = [1, 2, 3, 4, 5, 6, 7]
list_b     = [1, 2, 3, 4]
=================== result
summed_list  = [2, 4, 6, 8]

# Portuguese
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""


def create_list_with_summed_values(list_a, list_b):
    length = min(len(list_a), len(list_b))
    return [list_a[index] + list_b[index] for index in range(length)]


list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
print(create_list_with_summed_values(list_a, list_b))  # output: [2, 4, 6, 8]
