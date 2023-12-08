"""
# English
We can use @classmethod to create a factory method

The factory method will create instances from class with initial data already defined.

On example below, the class will begin with 50 years old always we call the factory method.

# Portuguese
Podemos usar @classmethod para fazer um metodo fabrica (factory_method)

O metodo fabrica vai criar instancias da classe pre iniciada.

No caso do exemplo abaixo, a classe serah iniciada com a idade 50 sempre que chamarmos o metodo fabrica.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        print('Hello World')

    @classmethod
    def method_factory(cls, name):
        return cls(name, 50)


p = Person.method_factory('John')
print(vars(p))  # output: {'name': 'John', 'age': 50}
