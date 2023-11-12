"""
Logical Operator 'OR'

With 'OR' if one condition is True then the expression will return True already
"""

condition_true = True
condition_false = False

if condition_true or condition_false:
    print('Will print line 11')

if condition_false or condition_false:
    print('Will not print')

if condition_true:
    print('Will print line 17')

print(False or False or False or 'ABC')
print(False or 'ABC')
