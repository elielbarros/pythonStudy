for raw in range(20):
    if raw % 2 == 0:
        continue

    if raw == 19:
        break

    print(f'[{raw}]', end=' ')

    for column in range(4):
        print(f'{column}', end=' ')

    print()

"""Today I Learned that is possible to use continue and break with for as shown above"""
