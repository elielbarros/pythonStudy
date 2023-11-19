"""
'YIELD FROM'

Delegate the generation to another iterable object.
"""


def generator_():
    for i in range(3):
        yield i


def generator_2():
    for j in generator_():
        yield j


def generator_3():
    yield from generator_()
    for i in range(3, 6):
        yield i


for value in generator_2():
    print(value)
    # output:
    # 0
    # 1
    # 2

    print()

for value in generator_3():
    print(value)
    # output
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
