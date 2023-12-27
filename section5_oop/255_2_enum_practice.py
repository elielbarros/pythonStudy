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


# This is not the best way to use enum
# Directions = enum.Enum('Directions', ['FORWARD', 'BACK', 'LEFT', 'RIGHT'])
# This is the best way to use enum
class Directions(enum.Enum):
    # It is possible to use enum.auto() to let enum enumerate each value we use
    FORWARD = enum.auto()
    BACK = 2
    LEFT = '3'


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Please provide a valid directin')

    print(f'Move {direction.name}')


move(Directions.FORWARD)
move(Directions.BACK)
move(Directions.LEFT)