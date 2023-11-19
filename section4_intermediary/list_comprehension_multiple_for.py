list_ = []

for x in range(2):
    for y in range(2):
        list_.append((x, y))

print(*list_, sep='\n')
# output:
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)

print()

# To do the same output using list comprehension,
# We can use two for as above
list_ = [
    (x, y)
    for x in range(2)
    for y in range(2)
]
print(*list_, sep='\n')
# output:
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)

print()

# We can also do a list comprehension considers another list comprehension.
# So an action B will be executed considering the action A
# If action A will be executed 3 times, then execute action B those 3 times,
# And this action B could be, for example, another list comprehension
list_ = [
    [letter for letter in 'John']
    for x in range(3)
]
print(*list_, sep='\n')
# output:
# ['J', 'o', 'h', 'n']
# ['J', 'o', 'h', 'n']
# ['J', 'o', 'h', 'n']
# What happened was that for each x, the list comprehension that is iterating over 'John' happens

print()

# We could also see that each action B is considering action A
# For example:
list_ = [
    [(x, letter) for letter in 'John']
    for x in range(3)
]
print(*list_, sep='\n')
# output:
# [(0, 'J'), (0, 'o'), (0, 'h'), (0, 'n')]
# [(1, 'J'), (1, 'o'), (1, 'h'), (1, 'n')]
# [(2, 'J'), (2, 'o'), (2, 'h'), (2, 'n')]
