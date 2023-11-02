"""
Comparison operator will return boolean

> represent 'Greater Than'
>= represent 'Greater or Equal Than'
< represent 'Less Than'
<= represent 'Less or Equal Than'
== represent 'Equal'
!= represent 'Different'
"""
one = 1
two = 2
a = 'a'
b = 'b'

greater_than = two > one
print(f'{two} is greater than {one}? {greater_than}')

greater_equal = two >= two
print(f'{two} is greater or equal than {two}? {greater_equal}')

greater_equal_1 = two >= one
print(f'{two} is greater or equal than {one}? {greater_equal_1}')

less_than = one < two
print(f'{one} is less than {two}? {less_than}')

less_equal = one <= one
print(f'{one} is less or equal than {one}? {less_equal}')

less_equal_1 = one <= two
print(f'{one} is less than {two}? {less_equal_1}')

equal = one == one
print(f'{one} is equal {one}? {equal}')

different = two != one
print(f'{two} is different of {one}? {different}')

equal_character = a == a
print(f'{a} is equal {a}? {equal_character}')

different_character = a != b
print(f'{a} is different {b}? {different_character}')
