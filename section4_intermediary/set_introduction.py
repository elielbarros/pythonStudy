"""
Sets - Python

Graphically represented by Venn diagram

Sets in python are mutable, but accept only immutable values as intern value.
"""

# How to create Set
set_ = set()
print(set_, type(set_))  # output: set() <class 'set'>

# Set does not have a key
# Set has only value
# Set will not guarantee element order
# Set will iterate over str
set_ = set('John')
print(set_, type(set_))  # output: {'n', 'h', 'o', 'J'} <class 'set'>

# If we want to set the string 'John' so we have to use {}
set_ = {'John'}
print(set_, type(set_))  # output: {'John'} <class 'set'>






