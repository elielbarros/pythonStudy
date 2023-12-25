"""
# English

# Portuguese
Toda classe criada herda, por padrao, de object e a metaclasse eh type.

Toda metaclasse precisa herdar de type.
"""


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class MyMetaClass(type):
    # Dunder __new__ Create and return the class on Metaclass
    def __new__(mcs, name, bases, dct):
        print('NEW METACLASS')
        cls = super().__new__(mcs, name, bases, dct)
        cls.__repr__ = my_repr

        if 'talk' not in cls.__dict__ or not callable(cls.__dict__['talk']):
            raise NotImplementedError('It is necessary to implement method talk')
        return cls

    # Dunder __call__ create and return the instance
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        if 'name' not in instance.__dict__:
            raise NotImplementedError('It is necessary to create attribute name')

        return instance


class Person(object, metaclass=MyMetaClass):
    def __new__(cls, *args, **kwargs):
        print('NEW')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('INIT')
        self.name = name

    def talk(self):
        print(f'{self.name} is Talking')


p = Person('John')
print(p)  # output: Person({'name': 'John'})

p.talk()  # output: John is Talking
