"""
# English
The Class has your own Scope.

Class Methods could make a reference to Class Scope and your own scope.

The parameters inserted in the class, using the recourse 'self', are parameters on the Class Scope and these
parameters are accessible from any method that belong to the class

The parameters defined only on method, will not be available inside another methods because these parameters belongs
to the method scope only.

# Portuguese
A classe tem escopo proprio.

Os metodos de uma classe tem referencia ao escopo da classe e do proprio metodo.

Os parametros que sao inseridos, utilizando o recurso 'self' da classe, sao parametros de escopo de classe e
acessiveis em qualquer metodo pertencente a classe

Os parametros que sao definidos apenas no metodo, nao ficará disponivel em outros metodos pq sao parametros
que pertencem ao escopo do metodo e nao pertence ao escopo da classe
"""


class Animal:
    # This variable is on Class Scope
    name_class_scope = 'Lion'

    def __init__(self, name):
        # This variable is on Class Scope
        self.name = name
        # This variable is on Method Scope only
        variable = 'value'
        print(variable)

    def eating(self, food):
        # We cant try to access variable declared on __init__ method because is out of scope
        # print(variable)  #  NameError: name 'variable' is not defined.
        print(f'{self.name} is eating {food}')


print(Animal.name_class_scope)
cat = Animal('Milk')
cat.eating('cat food')
