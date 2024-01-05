"""
# English
namedtuples
    - immutable tuple with names for values
    - We use namedtuples to create object classes that are just a grouping of attributes, like normal classes without
      methods, or database records, etc.

# Portugues
namedtuples
    - Tuplas imutaveis com nomes para valores
    - Usamos namedtuples para criar classes de objetos que sao apenas um agrupamento de atributos, como classes
      normais sem metodos, ou registros de bases de dados, etc.
"""
from collections import namedtuple

Player = namedtuple('Player', ['number', 'team'], defaults=[0, 'TEAM NAME'])

messi = Player(10, 'Argentina')

print(messi)  # output: Player(number=10, team='Argentina')
print(messi.number)  # output: 10
print(messi.team)  # output: Argentina
print(messi[0])  # output: 10
print(messi[1])  # output: Argentina
print(messi._fields)  # output: ('number', 'team')
print(messi._field_defaults)  # output: {'number': 0, 'team': 'TEAM NAME'}
print(messi._asdict())  # output: {'number': 10, 'team': 'Argentina'}
print(messi._field_types)


for value in messi:
    print(value)
    # output:
    # 10
    # Argentina
