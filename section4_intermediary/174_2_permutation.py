"""
# English
Permutation - itertools
Order matter here. Will repeat grouping by object.

# Portuguese
Permutation - itertools
Ordem importa. Repete os agrupamentos por objeto.
"""
from itertools import permutations
people = [
    'Sydney', 'Safa', 'Saoirse', 'Byron'
]

tshirt = [
    'black', 'white'
]

print(*permutations(people, 2), sep='\n')
# output:
# ('Sydney', 'Safa')
# ('Sydney', 'Saoirse')
# ('Sydney', 'Byron')
# ('Safa', 'Sydney')
# ('Safa', 'Saoirse')
# ('Safa', 'Byron')
# ('Saoirse', 'Sydney')
# ('Saoirse', 'Safa')
# ('Saoirse', 'Byron')
# ('Byron', 'Sydney')
# ('Byron', 'Safa')
# ('Byron', 'Saoirse')