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
from typing import NamedTuple


class Player(NamedTuple):
    number: int = 0
    team: str = 'TEAM'


messi = Player(10, 'Argentina')
print(messi)  # output: Player(number=10, team='Argentina')
