"""
# English
__dict__ or vars(class_instance)

The attributes initialized with class could be accessed as a dictionary using the method __dict__ or vars()

We also can update this dictionary as a dict

# Portuguese
__dict__ or vars(class_instance)

Os atributos inicializados com a classe podem ser acessados como um dicionario usando o metodo __dict__ ou vars()

Nos tambem podemos atualizar esse dicionario como um dict, objeto do Python

"""


class Person:
    actual_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthday(self):
        return Person.actual_year - self.age


p1 = Person('John', 28)
print(p1.__dict__)  # output: {'name': 'John', 'age': 28}

# We can change one dict object
p1.__dict__['name'] = 'Mary'
print(p1.__dict__)  # Output: {'name': 'Mary', 'age': 28}

# We can add one object to dict
p1.__dict__['last_name'] = 'Roe'
print(p1.__dict__)  # Output: {'name': 'Mary', 'age': 28, 'last_name': 'Roe'}

# We can create one Person using dict
data = {'age': 14, 'name': 'Bob'}
p2 = Person(**data)
print(p2.__dict__)  # output: {'name': 'Bob', 'age': 14}

# We can delete an attribute
del p2.__dict__['age']
print(p2.__dict__)  # output: {'name': 'Bob'}

# Besides that, we also can use method var()
print(vars(p1))  # output: {'name': 'Mary', 'age': 28, 'last_name': 'Roe'}
