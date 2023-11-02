"""
  0   1   2  3  4  5  6  7  8  9  10  11
  H   e   l  l  o     W  o  r  l   d   !
-12 -11 -10 -9 -8 -7 -6 -5 -4 -3  -2  -1

substring [InitialIndex : FinalIndex: Pass]

Pass means how many numbers will be passed
Default is 1

"""

phrase = 'Hello World!'
print(phrase[4:6])  # Will print only 'o' from Hello because python does not consider the last number 6

print(phrase[4:7])  # Will print 'o W' from Hello World! but won't print the char 'o' from 'World'

print(phrase[::])  # Will return all phrase

print(phrase[:5])  # When we don't put the initial number, python will consider from 0. Will print 'Hello'

print(phrase[6:])  # When we don't put the final number, python will consider string last index. Will print 'World!'

print(phrase[6::2])  # Will only print 'W r d' from 'World!'

# It is possible to reverse phrase using pass -1
print(phrase[-12::1])
