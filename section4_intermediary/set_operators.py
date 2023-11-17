"""
Set - Operators

It is possible to use some useful operators with 'Set'

UNION |, INTERSECTION &, DIFFERENCE -, SYMMETRIC DIFFERENCE ^
"""

# UNION
# It is possible to une different 'Sets' values.
# To do that, we will use the operator | representing UNION
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_result = set_a | set_b
print(set_result)  # output: {1, 2, 3, 4}

# INTERSECTION
# It is possible to get the intersection between two 'Set'.
# The intersection will return only values that are repeated into set_a and set_b
# To do that we have to use the operator &
set_result = set_a & set_b
print(set_result)  # output: {2, 3}

# DIFFERENCE
# The difference between two 'Set' will result into a Set with the values from set_a that is not in set_b,
# but it will return only set_a values.
set_result = set_a - set_b
print(set_result)  # output: {1}

# SYMMETRIC DIFFERENCE
# The 'symmetric difference' is likely 'difference' but will return everything that is not equal between
# set_a and set_b.
set_result = set_a ^ set_b
print(set_result)  # output: {1, 4}
