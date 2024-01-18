"""
# English
 - random -

The module 'random' provide functions to generate pseudorandom numbers.

doc: https://docs.python.org/pt-br/3/library/random.html

# Portuguese
 - random -

o módulo random fornece funções para gerar números pseudoaleatórios.

doc: https://docs.python.org/pt-br/3/library/random.html
"""
import random

# random.shuffle
# random shuffle will shuffle a list
names = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(names)
print(names)

# random.sample(iterable, k=N)
# random sample will shuffle a list and get N items from this list and return it as a newer list
# k <= len(iterable)
new_names = random.sample(names, k=2)
print(new_names)  # output: ['Joana', 'Helena']

# random.choices(iterable, k=N)
# It is similar to sample but eventually choices could return a list with equal values
new_names = random.choices(names, k=2)
print(new_names)  # output: ['Luiz', 'Luiz']

# random.choice(iterable)
# Will choice one value from iterable and return it
name = random.choice(names)
print(name)  # output: Joana
