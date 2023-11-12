"""
Introduction for try/except

Try -> Will try to execute the code

Except -> Will catch any error while trying to execute the code
"""

# It is possible to check if a INTEGER number typed on input is a digit. Example:
number_str = input('Type a number: ')
print(number_str.isdigit())

# But if you type a FLOAT number, the method is digit will not work
float_number_str = '2.3'
print(float_number_str.isdigit())

# We can work with try/except and check if was typed a number INTEGER/FLOAT
try:
    float_number_str = input('Type a float number: ')
    float_number = float(float_number_str)
    print(f'Float Number: {float_number}')
except:
    print('It is not a number')
