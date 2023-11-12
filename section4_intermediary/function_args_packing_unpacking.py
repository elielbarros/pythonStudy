"""
args - Not Named Arguments

* - *args (packing and unpacking)
"""


def sum_(*args):
    # args is a Tuple
    print(args, type(args))
    accumulator = 0
    # We can iterate over Tuple
    for argument in args:
        accumulator += argument
    return accumulator


result = sum_(1, 2, 3, 4, 5)
print(f'{result=}')

# We have a similar method in Python called sum,
# but a 'sum' receives one element. If you try to pass all elements inside tuple, it will raise the error:
# TypeError: sum() takes at most 2 arguments (5 given)
numbers = 1, 2, 3, 4, 5
print(numbers, type(numbers), *numbers)
# print(f'{sum(*numbers)=}')
# But if we call just numbers, that is iterable, a 'sum' will work
print(f'{sum(numbers)=}')
