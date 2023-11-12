"""
Repetitions

While

Execute an action While a condition is True
"""

index = 5

while index > 0:
    index = index - 1
    print(index)

condition = True
while condition:
    name = input('What is your name? ')
    print(f'Your name is {name}')
    if name == 'exit':
        break

print('Finish')


