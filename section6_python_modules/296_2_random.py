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

# Everything is aleatory because of 'seed'
# seed use time to make everything aleatory time.time()
#time_ = time.time()  # Return the current time in seconds
#random.seed(time_)
#print(time_)
# If we determine the 'seed', everything generated will not be aleatory
# Then everything will be the same value always
random.seed(0)

names = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(names)
print(names)

new_names = random.sample(names, k=2)
print(new_names)

new_names = random.choices(names, k=2)
print(new_names)


name = random.choice(names)
print(name)
