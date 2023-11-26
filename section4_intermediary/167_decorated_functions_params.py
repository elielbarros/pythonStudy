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


def decorated_function_factory(a, b, c):
    print('Decorated Function Factory')

    def function_factory(function):
        print('Function Factory')

        def inner_function(*args, **kwargs):
            print('Inner function')
            print('Decorated Function Factory Arguments:', a, b, c)
            res = function(*args, **kwargs)
            return res

        return inner_function

    return function_factory


@decorated_function_factory(1, 2, 3)
def sum_(a, b):
    return a + b


ten_plus_five = sum_(10, 5)
print(ten_plus_five)
# output:
# Decorated Function Factory
# Function Factory
# Inner function
# Decorated Function Factory Arguments: 1 2 3
# 15

decorated_factory = decorated_function_factory(1, 2, 3)
multiply_ = decorated_factory(lambda a, b: a * b)
print(multiply_(10, 5))
