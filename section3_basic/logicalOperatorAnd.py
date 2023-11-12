"""
Logical Operator 'AND'

With 'AND' all operations need to be True to return True
If one operation come False then the result will be False
"""
condition_true = True
condition_false = False

# 'IF' that will return 'False' because of 'condition_false'
if condition_true and condition_false:
    print('Will not print line 12')  # Will not print

if condition_true and condition_true:
    print('Will print line 17')

# short circuit assessment
# Will get off from if at the first condition false
if condition_false and condition_true:
    print('Will not print line 18')
