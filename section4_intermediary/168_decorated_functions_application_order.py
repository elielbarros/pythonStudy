"""
Decorated Function Order
English:
The order that Python uses to execute each Decorated Function is from bottom to top.
You can see the output of our test run below:

Portuguese:
A ordem que o python utiliza para executar cada Decorated Function é de baixo para cima.
É possível observar no output do nosso teste executado abaixo:
"""


def decorator_param(name):
    def decorator(function):
        print('Decorator:', name)

        def inner_function(*args, **kwargs):
            res = function(*args, **kwargs)
            final = f'{res} {name}'
            return final

        return inner_function

    return decorator


@decorator_param(name='second')
@decorator_param(name='first')
def sum_(a, b):
    return a + b


ten_plus_five = sum_(10, 5)
print(ten_plus_five)
# output:
# Decorator: first
# Decorator: second
# 15 first second
