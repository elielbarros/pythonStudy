"""
Function

To define a function with Python you must use 'def function_name()'

Function is commonly used for doing a specific action by calling.

Function can receive a param 'def function_name(param)'

Function can return a value after your process

Function for default return None
"""


def print_hello_world():
    print('Hello world!')


print_hello_world()


def print_param(param):
    print(param)


print_param('print param')

print(type(print_param('')))


def sum_(value_a, value_b):
    return value_a + value_b


print(sum_(1, 2), type(sum_(1, 2)))
