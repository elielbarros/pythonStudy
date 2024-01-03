"""
# English
Syntax Sugar - dataclass

The dataclass annotation will create getter, setter, __repr__ and __eq__ automatically.

It is available from Python 3.7

It is possible to create property and setter, even using dataclass annotation.

# Portuguese
Syntax Sugar - dataclass

A anotacao dataclass vai criar getter, setter, __repr__ e __eq__ da classe automaticamente.

Disponivel a partir do Python 3.7

Eh possivel criar property e setter normalmente, mesmo utilizando a anotacao dataclass.
"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    last_name: str
    age: int

    def get_complete_name(self):
        return f'{self.name} {self.last_name}'


p1 = Person('John', 'Doe', 13)
print(p1)  # output: Person(name='John', last_name='Doe', age=13)
print(p1.name)  # output: John
print(p1.age)  # output: 13

p2 = Person('Mary', 'Jane', 16)
print(p1 == p2)  # output: False
