"""
Formatação básica de strings
s - string
d - int
f - float
.<number of digits>f
x ou X - Hexadecimal
(Character)(><^)(Quantity)
> - Left
< - Right
^ - Center
= - Will force Positive and Negative signal to be before number
Signal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variable = 'O'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}.')
print(f'.{variable: ^9}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'The hexadecimal of 1500 is {1500:08X}')
print(f'{variable!r}')
