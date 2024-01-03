"""
# English
dunder __post_init__ performs an action after class initialization

If it is decided not to use __init__, put init=False in the dataclass argument

It is not possible to implement __init__ and __post_init__ together.

# Portuguese
dunder __post_init__ executa uma acao apos inicializacao da classe

Se for decidido nao usar o __init__, colocar no argumento de dataclass init=False

Nao eh possivel implementar __init__ e __post_init__ juntos.
"""

from dataclasses import dataclass


@dataclass(init=False)
class Person:
    name: str
    last_name: str
    age: int

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # def __post_init__(self):
    #     self.complete_name = f'{self.name} {self.last_name}'


p1 = Person('John', 'Doe', 20)
print(p1)  # Person(name='John', last_name='Doe', age=20)

print(p1.complete_name)
