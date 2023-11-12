"""
Assignment Operators
1. =
2. +=
3. -=
4. *=
5. /=
6. //=
7. **=
8. %=
"""
string = 'A'
string += 'B'
print(f'Concatenate element: {string}')


sum_element = 0
sum_element += 1
print(f'Sum element: {sum_element}')

subtract = 1
subtract -= 1
print(f'Subtract element: {sum_element}')

multiply = 2
multiply *= 2
print(f'Multiply element: {multiply}')

divide = 1
divide /= 1
print(f'Divide element: {divide}')

divide_truncate = 5
divide_truncate //= 2
print(f'Divide and truncate element: {divide_truncate}')

number_raised = 2
number_raised **= 2
print(f'Number raised element: {number_raised}')

module = 2
module %= 2
print(f'Module element: {module}')

