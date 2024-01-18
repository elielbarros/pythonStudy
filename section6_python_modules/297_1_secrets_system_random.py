"""
# English
- secrets -
provides functions to generate pseudorandom numbers intended for security purposes, such as generating passwords or
cryptographic tokens

# Portuguese
- secrets -

Fornece funções para gerar números pseudoaleatórios destinados a fins de segurança, como a geração de senhas ou
tokens criptográficos
"""
import secrets

# secrets.randbelow(exclusive_upper_bound)
# Will return a number below the number sent as parameter
s = secrets.randbelow(100)
print(s)  # output: 38

# secrets.choice(list)
# Will return an random element from the list provided
list_ = [10, 11, 12]
s = secrets.choice(list_)
print(s)




