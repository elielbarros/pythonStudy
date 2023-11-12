"""
It is possible to define a default value for a function.

def my_function(argument=None)

On this case, argument has the default value 'None'

When an argument is set with a default value, another argument after this first, need to receive a default value

def my_function(argument=None, second_argument=mandatory_value_here
"""


def sum_(a=0, b=0):
    print(a + b)


sum_()
sum_(b=2, a=1)
sum_(1, 2)


# As said before, on this case, the sum_ function will raise an error in case 'b' do not receive a default value
# def sum_(a=0, b):
#     print(a + b)
