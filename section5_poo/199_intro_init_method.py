"""
# English

We can initialize class with pre-defined attributes.

The method __init__ will receive by default the paremeter 'self' that does not need to be filled during your instance.
Only will be filled the attributes.

These attributes need to be initialized inside defined method, __init__ using 'self' for these attribute definitions

# Portuguese

Podemos inicializar a classe com atributos pre definidos

O metodo __init__ recebe por padrao o parametro 'self', que nao precisa ser preenchido durante a sua instancia,
apenas deve ser preenchido os atributos

Os atributos precisam ser inicializados dentro do metodo definido, __init__ usando o self para as definicoes dos
atributos
"""


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


p1 = Person('John', 'Doe')
print(p1.name)
print(p1.last_name)
