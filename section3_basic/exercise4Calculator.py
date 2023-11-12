import time

operator_group = '+-*/'

while True:
    exit_str = input('Press E to exit ')
    exit_str = exit_str.lower()
    exit_boolean = exit_str.startswith('e')

    if not exit_boolean:
        numberA_str = input('Type a number: ')
        operator = input('Type an operator: + - * / ')
        numberB_str = input('Type another number: ')
        try:
            numberA = float(numberA_str)
            numberB = float(numberB_str)
        except:
            print('You must provide a valid number.')
            continue

        if operator == '+':
            print(f'{numberA} {operator} {numberB} = {numberA + numberB}')
        elif operator == '-':
            print(f'{numberA} {operator} {numberB} = {numberA - numberB}')
        elif operator == '*':
            print(f'{numberA} {operator} {numberB} = {numberA * numberB}')
        elif operator == '/':
            print(f'{numberA} {operator} {numberB} = {numberA / numberB}')
        else:
            if operator not in operator_group:
                print('You must provide a valid operator: + - * /')
            elif len(operator):
                print('You must provide only one operator')
            continue
    else:
        count = 0
        print('Exiting', end='')
        while count < 3:
            time.sleep(0.5)
            print('.', end='')
            count += 1
        break
