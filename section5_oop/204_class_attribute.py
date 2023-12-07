"""
# English
- Class Attribute
A default attribute available for any instance created by Person.

# Portuguese
- Class Attribute
Um atributo padrao disponivel para qualquer instancia criada pela classe 'Person'
"""


class Person:
    actual_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthday(self):
        # It is possible to use Class Attribute 'actual_year' with 'self' or with class name 'Person'
        # Person.actual_year
        return self.actual_year - self.age


p1 = Person('John', 28)
print(p1.get_birthday())

# We can also access this attribute without instantiating Class Person
print(Person.actual_year)
