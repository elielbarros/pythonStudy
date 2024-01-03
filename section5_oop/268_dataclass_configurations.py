"""
# English

# Portguese
frozen=True
 - Vai tornar os atributos da classe read-only.

repr=False
 - Vai desativar o metodo repr

order=True
 - Vai criar, automaticamente a condicional para ordernar a classe, quando executado sorted()
"""
from dataclasses import dataclass


@dataclass(frozen=True, repr=True, order=True)
class Person:
    name: str
    age: int


p1 = Person('John', 15)
print(p1)  # <__main__.Person object at 0x7f83233bb590>
# p1.name = 'Mary'  # cannot assign to field 'name'

p2 = Person('Mary', 53)

list_ = [p1, p2]

ordered_ = sorted(list_)
print(ordered_)  # output: [Person(name='John', age=15), Person(name='Mary', age=53)]

ordered_reverse = sorted(list_, reverse=True)
print(ordered_reverse)  # output: [Person(name='Mary', age=53), Person(name='John', age=15)]
