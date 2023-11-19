"""
Set - Comprehension
"""

# Creating a set using comprehension
set_ = {index for index in range(3)}
print(set_)  # output: {0, 1, 2}

print()

# MAP a set using comprehension
set_ = {
    index ** 2
    if index % 2 == 0 else index
    for index in range(3)
}
print(set_)  # output: {0, 1, 4}

print()

# FILTER a set using comprehension
set_ = {
    index ** 2
    if index % 2 == 0 else index
    for index in range(10)
    if index > 6
}
print(set_)  # output: {64, 9, 7}
