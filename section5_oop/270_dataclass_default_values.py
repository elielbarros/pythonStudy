"""
# English
- Default value
    1. Only works with immutable values (str, int, float, bool)
    2. After implement first default value, next attributes must have default value

-field()
     1. Used to give a default value to a mutable attribute.

- fields()
     1. It will list all fields and their default values and types

# Portuguese
- Valores padrao
    1. Funciona apenas para valores imutaveis
    2. Depois de implementar primeiro valor padrao, proximo atributo precisa ter um valor padrao

- field()
    1. Serve para dar valor padrao a um atributo mutavel.

- fields()
    1. Vai listar todos os campos e seus valores padroes e tipos
"""

from dataclasses import dataclass, field


@dataclass
class Person:
    name: str = 'Default Name'
    # It is possible to disable this field from repr
    # It is possible to disable this field from compare
    last_name: str = field(
            default='MISSING', repr=False, compare=False
    )
    age: int = 0
    # address: list[str] = [] # List is mutable and it is not possible to create default value to list
    # To do this it is necessary to use field()
    address: list[str] = field(default_factory=list)


p1 = Person()
print(p1)  # output: Person(name='Default Name', age=0, address=[])
# print(fields(p1))
