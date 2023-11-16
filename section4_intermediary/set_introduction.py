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
print(set_)  # output: {'n', 'h', 'o', 'J'}

# If we want to set the string 'John' so we have to use {}
set_ = {'John'}
print(set_)  # output: {1, 2, 3}

# It is possible to convert a list into Set
list_ = [1, 2, 3]
set_ = set(list_)
print(set_)  # output: {'John'}

# When convert a list, 'Set' will remove all repeated numbers
# But 'Set' will not guarantee element order
list_ = [1, 1, 2, 2, 3, 3]
set_ = set(list_)
print(set_)  # output: {1, 2, 3}
list_ = ['aaa', 'aaa', 'bbb', 'bbb', 'fff', 'fff']
set_ = set(list_)
print(set_)  # output: {'bbb', 'aaa', 'fff'}

# It is possible to iterate over 'Set'
set_ = {1, 2, 3}
for element in set_:
    print(element)  # output: 1 2 3

# It is possible to check if 'Set' has the element
print(1 in set_)  # output: True

# It is not possible to create 'Set' using a mutable element, like 'list', 'Set', 'dict' etc
# set_ = {[1, 2, 3]}
# print(set_)  # output: TypeError: unhashable type: 'list'
# set_ = {1, {'John'}}
# print(set_)  # output: TypeError: unhashable type: 'set'
# set_ = {1, {'dict': 1}}
# print(set_)  # output: TypeError: unhashable type: 'dict'

# 'Set' does not have Index
# set_ = {1, 2, 3}
# print(set_[0])  # output: TypeError: 'set' object is not subscriptable
