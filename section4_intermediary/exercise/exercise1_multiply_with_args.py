def multiply_numbers(*args):
    accumulator = 1
    for number in args:
        accumulator *= number
    return accumulator


result = multiply_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
