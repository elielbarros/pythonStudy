"""
Python Module Index: https://docs.python.org/3/py-modindex.html

Ways to import modules

Complete Way: import module_name
    - advantage: module namespace
    - disadvantage: big name

Object From Complete Way: from module_name import object_name_1, object_name_2
    - advantage: small name
    - disadvantage: Without module namespace

Alias for Complete Way: import module_name as alias_module_name

Alias for Object From Complete Way: from module_name import object_name_1 as alias_object_name_1

Bad practice: from module_name import *
    - advantage: will import everything from module, and you will have access to everything.
    - disadvantage: Will import everything including what you will not use.
"""

# Import Complete Way
import sys
print(sys.platform)  # output: linux

print()

# Object From Complete Way
from random import randrange
random_number = f'{randrange(0, 999999999)}'
print(random_number)  # output: 77392016

print()

# Alias for Complete Way
import decimal as my_decimal_alias
print(my_decimal_alias.Decimal('0.1'))  # output: 0.1

print()

# Alias for Object From Complete Way
from sys import exit as my_exit_alias
my_exit_alias()

# Bad Practice:
from copy import *