"""
# English
In Python to extend from another class is necessary pass the class object as parameter.

In Python exists an order to find for methods inside the classes that has a relation using Inheritance.
This order is called by 'Method Resolution Order' (MRO).

We could see this order using the method help(child_class_name_here)

Observe that all created classes extend from 'builtins.object'

# Portuguese
Em Python para estender de uma outra classe eh necessario passar o objeto da classe como parametro da classe.

Em Python existe uma ordem de busca por metodos nas classes que se relacionam atraves de heranca.
O nome dado a essa ordem eh 'Method Resolution Order' (MRO).

Nos podemos ver essa ordem usando o metodo help(classe_filha_aqui)

Observe que toda classe criada estende de 'builtins.object'
"""


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def show_class_name(self):
        print('Show Class Name Method from Super Class Person')
        print(self.name, self.last_name, self.__class__.__name__)


class Client(Person):
    def show_class_name(self):
        print('If the same method is inside child class and super class, first method called will follow MRO order.')
        print(self.name, self.last_name, self.__class__.__name__)


class Employee(Person):
    ...


client_ = Client('John', 'Doe')
employee_ = Employee('Zoe', 'Cardenas')

client_.show_class_name()
# output:
# If the same method is inside child class and super class, first method called will follow MRO order.
# John Doe Client

employee_.show_class_name()
# output:
# Show Class Name Method from Super Class Person
# Zoe Cardenas Employee

# help(Client)
# part of output:
# Method resolution order:
# - Client
# - Person
# - builtins.object
