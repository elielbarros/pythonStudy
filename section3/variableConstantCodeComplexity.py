"""
CONSTANT is a property that won't change
CONSTANT does not exist in python
But is normal to see a property in UPPERCASE that indicates this property is a constant.

It is important to avoid so many conditions on if because of complexity
Example:
if condition and condition1 and condition2 and condition3 and condition4

The further the code is to the left, more complex it is
Example:
if condition:
    if condition:
        if condition:

The code must be easy to read. Avoid these complexity.
"""
MAX_SPEED = 100
PEOPLE_OVER_18 = 18

car_speed = 200
boy_age = 14

if car_speed > MAX_SPEED:
    print('The car is over max speed.')

if boy_age > PEOPLE_OVER_18:
    print('Boy is over 18.')
