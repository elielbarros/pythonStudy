def sum_(x, y):
    return x + y


def multiply(x, y):
    return x * y


def execute_function(function, x):
    def intern_function(y):
        return function(x, y)
    return intern_function


sum_with_five = execute_function(sum_, 5)
print(sum_with_five(5))  # output: 10

multiply_by_ten = execute_function(multiply, 10)
print(multiply_by_ten(10))  # output: 100
