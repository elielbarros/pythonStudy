"""
How works Generator
"""

def generator_(n=0):
    yield 1  # pause
    print("continue...")
    yield 2  # pause
    print('One more...')
    yield 3
    print('Finish')
    return 'It is over'

gen = generator_(n=0)
print(next(gen))  # output: 1
print(next(gen))  # output: 2
print(next(gen))  # output: 3
# print(next(gen))  # output: StopIteration: It is over

print()

# How does this dynamically
gen = generator_(n=0)
for i in gen:
    print(i)
    # output
    # 1
    # continue
    # ...
    # 2
    # One more...
    # 3
    # Finish

print()

def range_generator(n=0, maximum=10):
    while True:
        yield n

        if n == maximum:
            return

        n += 1

gen = range_generator(0, 10)
for n in gen:
    print(n)
    # output
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10