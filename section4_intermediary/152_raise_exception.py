"""
raise: raise will throw an exception
Exceptions: DOCUMENTATION: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
"""

string_ = ''

# It is possible to interrupt the action that we dont want raising something an error
# if not string_:
#     raise ValueError('string is empty')
# output:

# Traceback (most recent call last):
#   File "/home/eliel/Documents/projects/pythonStudy/section4_intermediary/152_raise_exception.py", line 9, in <module>
#     raise ValueError('string is empty')
# ValueError: string is empty


# It is possible to get the exception and raise it again
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise


print(divide(1, 0))

# output:
# Traceback (most recent call last):
#   File "/home/eliel/Documents/projects/pythonStudy/section4_intermediary/152_raise_exception.py", line 26, in <module>
#     print(divide(1, 0))
#           ^^^^^^^^^^^^
#   File "/home/eliel/Documents/projects/pythonStudy/section4_intermediary/152_raise_exception.py", line 21, in divide
#     return a / b
#            ~~^~~
# ZeroDivisionError: division by zero

