"""
Search for: 'Algoritmo de Validação do CPF'

CPF: 746.824.890-70
"""

cpf = '746.824.890-70'
split_cpf = cpf.split('-')
substring_cpf = cpf[:11]
numbers_to_multiply = 10
sum_ = 0
for digit in split_cpf[0]:
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

first_number = sum_ * 10 % 11
if first_number > 9:
    print(0)
else:
    print(first_number)
