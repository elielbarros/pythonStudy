"""
# English
Abstract classes - Abstract Base Class (abc)

ABCs are used as contracts for defining new classes. They can force other classes to create concrete methods. They
may also have concrete methods of their own.
@abstractmethods are methods that have no content.
The rules for abstract classes with abstract methods is that they CANNOT be instantiated directly.
Abstract methods MUST be implemented in subclasses (@abstractmethod).
An abstract class in Python has its metaclass being ABCMeta.
It is possible to create @property @setter @classmethod @staticmethod and @method as abstract, for this use
@abstractmethod as the innermost decorator.

# Portuguese
Classes abstratas - Abstract Base Class (abc)

ABCs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos
concretos. Também podem ter métodos concretos por elas mesmas.
@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.
Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.
É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod
como decorator mais interno.
"""
from abc import ABC, abstractmethod


# ABC is a class that has a Metaclass ABCMeta
# What we want is create a class that has as Metaclass ABCMeta
# We also could create a class like that: class Log(metaclass=ABCMeta) but we have to import ABCMeta
# For a class to be abstract we must inherit from ABC and have at least one abstract method defined
class Log(ABC):
    @abstractmethod
    def _log(self, message): ...


# Now if we try to create an instance from Log we will have an error.
# log_ = Log()  # output: TypeError: Can't instantiate abstract class Log with abstract method _log

# Now if we want to use Log methods, we have to create a class that extends from Log and implement methods.
# We have to implement methods from abstract class, necessarily
class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')

