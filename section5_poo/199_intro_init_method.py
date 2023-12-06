"""
# English

We can initialize class with pre-defined attributes.

The method __init__ will receive by default the paremeter 'self' that does not need to be filled during your instance.
Only will be filled the attributes.

These attributes need to be initialized inside defined method, __init__ using 'self' for these attribute definitions

Initialized attributes that use 'self.' in the beginning, are defining the class attributes with the attributes
passed as a parameter

In the example below, we are defining the 'name' and 'last_name' attributes with the parameters 'name_param' and
'last_name_param'.

The attributes that came in the parameter do not need to have the same name as the attributes that belong to the class

# Portuguese

Podemos inicializar a classe com atributos pre definidos

O metodo __init__ recebe por padrao o parametro 'self', que nao precisa ser preenchido durante a sua instancia,
apenas deve ser preenchido os atributos

Os atributos precisam ser inicializados dentro do metodo definido, __init__ usando o self para as definicoes dos
atributos

Os atributos inicializados que utilizam 'self.' no inicio, estao definindo os atributos da classe com os atributos
passados como parametro

No exemplo abaixo, estamos definindo os atributos 'name' e 'last_name' com os parametros de mesmo nome,
'name' e 'last_name'.

Os atributos que vieram no parametro nao precisam ter o mesmo nome dos atributos que pertencem a classe
"""


class Person:
    def __init__(self, name_param, last_name_param):
        self.name = name_param
        self.last_name = last_name_param


p1 = Person('John', 'Doe')
print(p1.name)
print(p1.last_name)
