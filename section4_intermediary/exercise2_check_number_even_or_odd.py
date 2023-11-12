def even_or_odd(*args):
    accumulator = []
    for element in args:
        if element % 2 == 0:
            accumulator.append(f'{element} is even')
            continue

        accumulator.append(f'{element} is odd')
    return accumulator


result = even_or_odd(1, 2, 3, 4, 5, 6)
for element in result:
    print(element)
