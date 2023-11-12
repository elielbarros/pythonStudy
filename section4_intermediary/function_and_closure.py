"""
Closure And Functions that will return others functions.

A closure allows a function to capture local variables from an external function, even if that external function has
already finished executing.
"""


def multiplier(n):
    def intern_function(x):
        return x * n

    return intern_function


# Creating Functions using Closure
double = multiplier(2)
triple = multiplier(3)
quadrature = multiplier(4)

# Calling Functions
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
print(quadrature(2))  # Output: 8

for number in [1, 2, 3, 4, 5]:
    print(f'{double(number)=}')

for number in [1, 2, 3, 4, 5]:
    print(f'{triple(number)=}')
