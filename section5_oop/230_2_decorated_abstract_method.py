"""

"""
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self): return self._name

    """If we do not want getter as abstract method, but we want setter as abstract method, then inside class that is 
    extending from AbstractFoo will have to implement setter but rather than use '@name.setter' it will be necessary 
    to use abstract class name"""
    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
