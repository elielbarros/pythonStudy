"""
Logical Operator 'NOT'

With 'NOT' it is possible to reverse the boolean value from True to False and Vice Versa
not True = False
not False = True
"""

condition_true = True
condition_false = False

if condition_true and not condition_false:
    print('Will print line 11')

print(False or not False)

print(True and not True)
print(True and not False)

