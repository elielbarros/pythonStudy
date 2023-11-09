"""
inaccuracy in float numbers

Double-precision Floating-point format IEEE 754
"""
import decimal

number_a = 0.1
number_b = 0.7
sum_ = number_a + number_b

print(sum_)  # It will print 0.7999999999999999

# To print as expected
print(f'{sum_:.2f}')  # It will print exactly 0.80

# Using method round() to print as expected
print(round(sum_, 2))

# To calculate precisely it is possible to use decimal class
number_a = decimal.Decimal(0.1)
number_b = decimal.Decimal(0.7)
sum_ = number_a + number_b
print(sum_)

# It is possible to sum decimal.Decimal() with value as string type and it will return value expected
number_a = decimal.Decimal('0.1')
number_b = decimal.Decimal('0.7')
sum_ = number_a + number_b
print(sum_)
