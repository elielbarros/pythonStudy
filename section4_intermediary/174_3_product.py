"""
# English
Permutation - itertools
Order matter here. Will repeat grouping by object.

# Portuguese
Permutation - itertools
Ordem importa. Repete os agrupamentos por objeto.
"""
from itertools import product


tshirt = [
    ['black', 'white'],
    ['s', 'm', 'l'],
    ['masculine', 'feminine']
]

print(*product(*tshirt), sep='\n')
