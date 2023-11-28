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
# output
# ('black', 's', 'masculine')
# ('black', 's', 'feminine')
# ('black', 'm', 'masculine')
# ('black', 'm', 'feminine')
# ('black', 'l', 'masculine')
# ('black', 'l', 'feminine')
# ('white', 's', 'masculine')
# ('white', 's', 'feminine')
# ('white', 'm', 'masculine')
# ('white', 'm', 'feminine')
# ('white', 'l', 'masculine')
# ('white', 'l', 'feminine')
