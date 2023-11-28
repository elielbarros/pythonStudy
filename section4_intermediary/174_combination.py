"""
# English
Combinations - itertools
Order does not matter here. We just have to combine objects with each other without repetition.

# Portuguese
Combinations - itertools
Ordem nao importa. Nos temos que combinar os objetos entre si sem repeticao.
"""
from itertools import combinations

people = [
    'Sydney', 'Safa', 'Saoirse', 'Byron'
]

tshirt = [
    'black', 'white'
]

# Here we want combinations between people in grouped by two
# So we can combine Sydney with Safa (two person)
# Safa with Saoirse (two person)
print(*combinations(people, 2), sep='\n')
# output
# ('Sydney', 'Safa')
# ('Sydney', 'Saoirse')
# ('Sydney', 'Byron')
# ('Safa', 'Saoirse')
# ('Safa', 'Byron')
# ('Saoirse', 'Byron')
