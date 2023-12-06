"""
# English

We can use our class to perform an action defining a method inside the class.

# Portuguese
Nos podemos usar nossa classe para executar uma acao usando um metodo definido na classe.

"""


class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating')


car_ = Car('Corvet')
car_.accelerate()
