"""
English:
Decorators are a powerful and flexible way to modify or extend the behavior of functions without changing their
actual code. Decorators are functions that take another function as an argument and return a new function that
usually extends or modifies the behavior of the original function.

Portuguese:
Decoradores são uma forma poderosa e flexível de modificar ou estender o comportamento de funções sem alterar seu
código real. Decoradores são funções que recebem outra função como argumento e retornam uma nova função que
geralmente estende ou modifica o comportamento da função original.
"""


def create_func(function):
    def inner_function(*args, **kwargs):
        for arg in args:
            print(arg)
            is_string(arg)
        result = function(*args, **kwargs)
        return result

    return inner_function


def revert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param must be a string')


revert_string_checking_param = create_func(revert_string)
reverted_string = revert_string_checking_param('123')
print(reverted_string)
