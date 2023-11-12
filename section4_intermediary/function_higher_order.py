"""
Function works as variable

It is possible to define a function and use it as a variable.

It is possible to pass a defined function as an argument for another function
"""


def salutation(argument):
    return argument


print(salutation('Hello world!'))

salutation_variable = salutation
print(salutation_variable('Hello World, Salutation Variable!'))


def execute_function(function_argument, salutation_argument):
    return function_argument(salutation_argument)


result = execute_function(salutation_variable, 'Hello World, Salutation Variable as argument inside execute function')
print(result)


# It is even possible to unpacking arguments with function as shown below:
def salutation_unpacking(message, name):
    return f'{message}, {name}!'


def execute_function_args(function_argument, *args):
    return function_argument(*args)


result = execute_function_args(salutation_unpacking, 'Hello', 'World')
print(result)
