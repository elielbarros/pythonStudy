"""
Search for: 'Algoritmo de Validação do CPF'

CPF: 746.824.890-70
"""
import re

cpf_replaced = '746.824.890-70'.replace('.', '').replace('-', '')
print(cpf_replaced)

# Regex will get everything that is not a number between 0 and 9 and replace for nothing
cpf_regex = re.sub(
        r'[^0-9]',
        '',
        '746.824.890-70'
)
print(cpf_regex)

cpf = '746.824.890-70'
substring_cpf = cpf[:11]
numbers_to_multiply = 10
sum_ = 0
for digit in substring_cpf:
    try:
        digit_int = int(digit)
        # print(digit_int)
        result_multiplication = digit_int * numbers_to_multiply
        # print(result_multiplication)
        numbers_to_multiply -= 1
        sum_ += result_multiplication
        # print(sum_)
    except ValueError as e:
        # print(e)
        continue

first_number = (sum_ * 10) % 11
if first_number > 9:
    print(0)
else:
    print(first_number)

substring_cpf = cpf[:13]
numbers_to_multiply = 11
sum_ = 0
for digit in substring_cpf:
    try:
        digit_int = int(digit)
        # print(digit_int)
        result_multiplication = digit_int * numbers_to_multiply
        # print(result_multiplication)
        numbers_to_multiply -= 1
        sum_ += result_multiplication
        # print(sum_)
    except ValueError as e:
        # print(e)
        continue

second_number = (sum_ * 10) % 11
if first_number > 9:
    print(0)
else:
    print(second_number)

