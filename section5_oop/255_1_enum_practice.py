"""
# English
Enum - Enumeration

Collection of named values, representing constants that should not be changed during program execution. Enums provide
a way to associate human-readable labels with integer values or strings, providing code clarity and readability.

Enum in Python is a class with a different Metaclass.

To get Enum data in Python
key = Class.key.name
value = Class.key.value

# Portuguese
Enum - Enumeracoes

Coleção de valores nomeados, representando constantes que não devem ser alteradas durante a execução do programa.
Enums oferecem uma maneira de associar rótulos legíveis a valores inteiros ou strings, proporcionando clareza e
legibilidade ao código.

Enum em Python eh uma classe com uma metaclasse diferente.

Para obter dados de um Enum em Python
chave = Classe.chave.name
valor = Classe.chave.value
"""
import enum

Directions = enum.Enum('Directions', ['FORWARD', 'BACK', 'LEFT', 'RIGHT'])

print(Directions(1), Directions['FORWARD'], Directions.FORWARD)
# output: Directions.FORWARD Directions.FORWARD Directions.FORWARD
print(Directions(1).name, Directions['FORWARD'].name, Directions.FORWARD.name)  # output: FORWARD FORWARD FORWARD
print(Directions(1).value, Directions['FORWARD'].value, Directions.FORWARD.value)  # output: 1 1 1


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Please provide a valid directin')

    print(f'Move {direction.name}')


move(Directions.FORWARD)
move(Directions.BACK)
move(Directions.LEFT)
move(Directions.RIGHT)
