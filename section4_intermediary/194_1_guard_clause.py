"""
# English


# Portuguese
"Guard Clause" (cláusula de guarda) é uma técnica que envolve verificar as condições especiais e casos limites
primeiro em uma função antes de continuar com o restante do código. O objetivo é lidar com casos excepcionais ou
condições inesperadas no início da função, tornando o código mais legível e evitando a execução desnecessária de código.

O uso de Guard Clauses pode melhorar a legibilidade do código, pois coloca as verificações de condições especiais no
início da função, destacando casos excepcionais antes de entrar na lógica principal da função.

Além disso, ao lidar com condições excepcionais precocemente, você pode evitar a execução desnecessária de código,
melhorando a eficiência em casos onde a função não precisa continuar com o processamento padrão.
"""


# EXAMPLE:
def calc_total_price(qtt_items, unitary_price):
    # Guard Clause 1
    if qtt_items <= 0:
        return 0  # If the quantity of items is not positive, so the total price is zero
    # Guard Clause 2
    if unitary_price < 0:
        raise ValueError('The unitary Price must be positive.')

    # Business Rule
    total_price = qtt_items * unitary_price
    return total_price
