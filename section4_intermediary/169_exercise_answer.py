def zipper(list1, list2):
    len_minimal_value = min(len(list1), len(list2))
    return [(list1[index], list2[index]) for index in range(len_minimal_value)]


list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(list1, list2))
# output: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
