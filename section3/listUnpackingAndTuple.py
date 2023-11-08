"""
Introduction to Unpacking and Tuple
It is possible to unpack a list into a tuple
"""
# Unpacking three elements from list into three variables
unpacked_1, unpacked_2, unpacked_3 = ['Hello', 'World', '!']

print(unpacked_1)
print(unpacked_2)
print(unpacked_3)

# It is not possible to unpack three elements into one variable only
# It will raise ValueError: too many values to unpack (expected 1)
# unpacked_1_error, = ['Hello', 'World', '!']

# It is not possible to unpack three elements from list into four variables
# It will raise ValueError: not enough values to unpack (expected 4, got 3)
# unpacked_1_error, unpacked_2_error, unpacked_3_error, unpacked_4_error = ['Hello', 'World', '!']

# It is possible to Unpack the first and second elements from list into two variables and the rest into one variable
# But it is necessary a special character before the variable
first, *rest = ['Hello', 'World', '!']
print(f'first: {first}')
print(f'rest: {rest}')  # Rest will be the rest of list AS A LIST


