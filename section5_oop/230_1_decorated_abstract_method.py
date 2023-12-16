"""

"""
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    # If we want to define how we will get the attribute inside the class that extend AbstractFoo
    @property
    @abstractmethod
    def name(self): ...

    @name.setter
    def name(self, name): ...


class Foo(AbstractFoo):
    # Another option is remove getter and setter and define property on class like:
    # name = ""
    def __init__(self, name):
        super().__init__(name)

    # Given that we create an abstract method name inside AbstractFoo we must define this method here
    # It is necessary define setter together or Python will raise an exception
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)