def execute_function(function_, *args):
    return function_(*args)


def sum_(x, y):
    return x + y


# Using lambda to work as a simple function
print(
        execute_function(
                lambda x, y: x + y,
                2, 3
        ),
        execute_function(sum_, 2, 3),
        sum_(2, 3)
)  # output: 5 5 5


# Using lambda to work as a complex function
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply


duplicate = create_multiplier(2)
print(duplicate(2))  # output: 4

duplicate = execute_function(
        lambda m: lambda n: n * m,
        2
)
print(duplicate(2))  # output: 4


# Using a method sum from python with lambda
print(
        execute_function(
                lambda *args: sum(args),
                1, 2, 3, 4, 5, 6, 7
        )
)
