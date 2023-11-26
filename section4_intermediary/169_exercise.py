"""
English:
Exercise - Joining Lists
Create a zipper function (like the clothes zipper).
The job of this function will be to join two lists in order.
Use all values from the shortest list.
Example:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Result
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')

Portuguese:
Exercicio - Unir Listas
Crie uma função zipper (como o zipper de roupas).
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
Exemplo:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')
"""


def check_smallest_name(value_a, value_b):
    if len(value_a) > len(value_b):
        return value_a, value_b
    return value_b, value_a


def check_smallest_list(list_a, list_b):
    if len(list_a) < len(list_b):
        return list_a, list_b
    return list_b, list_a


def join_list(list_a, list_b):
    smallest, biggest = check_smallest_list(list_a, list_b)
    count = 0
    result = []
    for item in smallest:
        city, state = check_smallest_name(item, biggest[count])
        result.append((city, state))
        count += 1
    return result


list_a = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_b = ['BA', 'SP', 'MG', 'RJ']

print(join_list(list_a, list_b))
# output: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
