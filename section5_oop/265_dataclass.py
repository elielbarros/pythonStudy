"""
# English

# Portuguese
Syntax Sugar - dataclass

A anotacao dataclass vai criar getter, setter, __repr__ e __eq__ da classe automaticamente.

Disponivel a partir do Python 3.7


"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p1 = Person('John', 13)
print(p1)  # output: Person(name='John', age=13)
print(p1.name)  # output: John
print(p1.age)  # output: 13

p2 = Person('Mary', 16)
print(p1 == p2)  # output: False
