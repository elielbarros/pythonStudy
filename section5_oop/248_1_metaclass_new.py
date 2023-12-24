"""
# English

# Portuguese
Toda classe criada herda, por padrao, de object e a metaclasse eh type.

Toda metaclasse precisa herdar de type.
"""


# Inherit from 'object' and set metaclass=type witch is the default value
class Foo(object, metaclass=type):
    ...


class MyMetaClass(type):
    def __new__(mcs, name, bases, dct):
        print('NEW METACLASS')
        cls = super().__new__(mcs, name, bases, dct)
        return cls


# It is possible as we use metaclass=type, create a class that will inherit from type and use this class instead of type
class Person(object, metaclass=MyMetaClass):
    def __new__(cls, *args, **kwargs):
        print('NEW')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('INIT')
        self.name = name


p1 = Person('John')

f = Foo()