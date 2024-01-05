"""
# English
- asdict(object)
    Will convert an object into dict

- astuple
    Will convert an object into tuple

# Portuguese
- asdict(object)
    Vai converter um objeto em um dicionario

- astuple
    Vai converter um objeto em uma tupla

"""

from dataclasses import asdict, astuple, dataclass


@dataclass
class Person:
    name: str
    age: int


p1 = Person('John', 10)
print(asdict(p1))  # output: {'name': 'John', 'age': 10}
print(astuple(p1))  # output: ('John', 10)
