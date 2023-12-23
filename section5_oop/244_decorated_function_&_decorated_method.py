# function that will be used as decorated function
def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


def show_planet(method):
    def inner_function(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if 'Earth' in result:
            return 'You are in home.'
        return result

    return inner_function


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


class Team(MyReprMixin):
    def __init__(self, name):
        self.name = name


class Planet:
    def __init__(self, name):
        self.name = name

    @show_planet
    def print_name(self):
        return f'The planet is {self.name}'


@add_repr
class Car:
    def __init__(self, name):
        self.name = name


# Using Inheritance to implement repr
brazil = Team('Brazil')  # output: Team({'name': 'Brazil'})
print(brazil)

# Using function to implement repr
Planet = add_repr(Planet)
earth = Planet('Earth')  # output: Planet({'name': 'Earth'})
print(earth)
print(earth.print_name())  # output: You are in home.

# Using decorated function to implement repr
creta = Car('Creta')  # output: Car({'name': 'Creta'})
print(creta)
