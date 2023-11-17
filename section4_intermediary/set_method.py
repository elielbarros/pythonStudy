"""
Set - Useful method

ADD, UPDATE, CLEAR, DISCARD
"""
set_ = set()
print(set_, type(set_))  # output: set() <class 'set'>

# ADD
# It is possible to add value into 'Set' using method .add()
# .add() method only add one argument at a time
set_.add('John')
print(set_)  # output: {'John'}

# UPDATE
# It is possible to insert new values into 'Set' updating the 'Set' actual state,
# But to use update we have to send iterable values. 'Iterable[str | int]'
set_.update(['Hello World', 1])
set_.update(('Doe', 2))
print(set_)  # output: {1, 2, 'Hello World', 'Doe', 'John'}

# If we put only string, 'Set' will mount the value iterating over each string letter
set_ = set()
set_.update('spelling')
print(set_)  # output: {'g', 'p', 'i', 'n', 'l', 'e', 's'}

# DISCARD
# It is possible to 'discard'/remove an element from 'Set'
# the method '.discard(argument)' is responsible for that.
# To do this, it is necessary to send the argument that we want to remove from 'set'
set_ = set()
set_.add('John')
print(set_)  # output before discard: {'John'}
set_.discard('John')

set_.update([1, 2])
print(set_)  # output after discard: {1, 2}

