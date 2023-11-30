"""
# English
Recursive Function - A function that calls itself at some point of execution until it finds the end of its
condition to terminate.

The limit to recursive function is 1000.

It is possible to change Recursive Function limit using library sys
import sys
sys.setrecursionlimit(1500)


# Portuguese
Funcao Recursiva - Uma funcao que chama a si propria em algum ponto de execucao até encontrar o fim da sua condicao
para finalizar.

O limite para recursividade eh de 1000.

Eh possivel mudar esse limite usando a biblioteca sys
import sys
sys.setrecursionlimit(1500)
"""
import sys
sys.setrecursionlimit(1500)

def calculate_factorial(number):
    if number == 0:
        return 1
    number *= calculate_factorial(number - 1)
    return number


print(calculate_factorial(5))  # output: 120
# print(calculate_factorial(1000))  # output: RecursionError: maximum recursion depth exceeded in comparison
print(calculate_factorial(1400))
