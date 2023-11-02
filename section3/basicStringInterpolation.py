"""
Basic String Interpolation

's'             - string
'd' and 'i'     - int
'f'             - float
'x' and 'X'     - Hexadecimal (ABCDEF0123456789)
"""

name = 'John'
price = 1000.95897643
phrase = '%s, the total price is $%f' % (name, price)
print(phrase)

phrase = '%s, the total price is $%.2f' % (name, price)
print(phrase)

phrase = 'Hexadecimal from %d is %X' % (15, 15)
print(phrase)
