"""
# English
count()
An iterative method that can be iterated

# Portuguese
count()
Um método iterativo que pode ser iterado

"""
from itertools import count

c1 = count()

print('c1', hasattr(c1, '__iter__'))  # output: c1 True
print('c1', hasattr(c1, '__next__'))  # output: c1 True

for index in c1:
    if index > 10:
        break
    print(index)  # output: 0 1 2 3 4 5 6 7 8 9 10

print()

# It is possible to start count(n) by a specific number
c1 = count(5)
for index in c1:
    if index > 10:
        break
    print(index)  # output: 5 6 7 8 9 10

print()

# It is possible to use a step with count(n, step)
# So count will be sum with 2 from zero
c1 = count(0, 2)
for index in c1:
    if index > 10:
        break
    print(index)  # output: 0 2 4 6 8 10

print()

# We could even use Named Argument
c1 = count(step=2, start=0)
for index in c1:
    if index > 10:
        break
    print(index)  # output: 0 2 4 6 8 10
