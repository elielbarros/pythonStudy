"""
# English

# Portuguese
Toda classe criada herda, por padrao, de object e a metaclasse eh type.

Toda metaclasse precisa herdar de type.
"""


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


# It is possible to execute tasks before create class, using Metaclass
# For example repr will be implemented before class creation
class MyMetaClass(type):
    def __new__(mcs, name, bases, dct):
        print('NEW METACLASS')
        cls = super().__new__(mcs, name, bases, dct)
        cls.__repr__ = my_repr

        # It is possible to make the class inheriting from class MyMetaClass to implement a method
        # For example, the class Person will be forced to implement the method talk
        if 'talk' not in cls.__dict__ or not callable(cls.__dict__['talk']):
            raise NotImplementedError('It is necessary to implement method talk')
        return cls


class Person(object, metaclass=MyMetaClass):
    def __new__(cls, *args, **kwargs):
        print('NEW')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('INIT')
        self.name = name

    # So now it is necessary to implement talk
    def talk(self):
        print(f'{self.name} is Talking')


# Even if the class Person is not instantiated
# It will be seen that the class MyMetaClass will execute the dunder __new__
# The output: NEW METACLASS

# After implement repr it will be possible to see repr working inside the class Person
p = Person('John')
print(p)  # output: Person({'name': 'John'})

p.talk()  # output: John is Talking
