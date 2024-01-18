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

# random.randrange(start, stop)
# Random number between 10 and 20 excluding 20
r = random.randrange(10, 20)
print(r)

# random.randrange(start, stop, step)
# Random number between 10 and 20 incrementing 3
r = random.randrange(10, 20, 3)
print(r)  # possible numbers: 13, 16, 19

# random.randint(start, stop)
# Random number between 10 and 20 including 20
r = random.randint(10, 20)
print(r)

# random.uniform(start, stop)
# Random float number between 10 and 20 excluding 20
r = random.uniform(10, 20)
print(r)


