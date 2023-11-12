from random import randrange

cpf = f'{randrange(0, 999999999)}'

while len(cpf) < 11:
    numbers_to_multiply = len(cpf) + 1
    sum_ = 0
    for digit in cpf:
        digit_int = int(digit)
        sum_ += digit_int * numbers_to_multiply
        numbers_to_multiply -= 1
    calc = (sum_ * 10) % 11
    number = f'{0 if calc > 9 else calc}'
    if len(cpf) == 9:
        cpf += number
        continue

    cpf += number

print(cpf)
