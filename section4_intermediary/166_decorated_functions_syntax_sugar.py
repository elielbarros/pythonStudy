"""
We can use Syntax Sugar with Decorated Functions

Syntax Sugar is basically use the Decorated Function with @ over method that we want
"""


def create_func(function):
    def inner_function(*args, **kwargs):
        print('Decorate')
        for arg in args:
            is_string(arg)
        result = function(*args, **kwargs)
        print('Decorated')
        return result

    return inner_function


@create_func
def revert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param must be a string')


reverted_string = revert_string('123')
print(reverted_string)
# output:
# Decorate
# Decorated
# 321
