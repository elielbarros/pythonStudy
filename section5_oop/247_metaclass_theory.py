"""
# English
Metaclasses are the type of classes
IN PYTHON, EVERYTHING IS AN OBJECT (CLASSES TOO)
So what is the type of a class? (type) TYPE is what generates the class
- Your object is an instance of your class
- Your class is an instance of type (type is a metaclass)
type('class_name', (Inheritances,), __dict__)

When creating a class, things happen by default in this order:
NOTE: The __new__ of the class creates and returns a new instance, the __new__ of the metaclass creates and returns CLASS
1. Metaclass's __new__ is called and creates the new class
2. __call__ of the metaclass is called with the arguments and calls:
     A. __new__ of the class with the arguments (creates the instance)
     B. __init__ of the class with the arguments
3. metaclass __call__ ends execution

Important metaclass methods
__new__(mcs, name, bases, dict) (Creates the class)
__call__(cls, *args, **kwargs) (Creates and initializes the instance)

"Metaclasses are deeper spells than 99% of users should care about. If you want to know if you need
they don't need them (people who really need them know for sure that they need them and don't need
an explanation as to why).”
— Tim Peters (CPython Core Developer)

object above
classFoo:
     ...

# Portuguese
Metaclasses são o tipo das classes
EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
Então, qual é o tipo de uma classe? (type) TYPE eh o que gera a classe
Seu objeto é uma instância da sua classe
Sua classe é uma instância de type (type é uma metaclass)
type('Name', (Bases,), __dict__)

Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
1. __new__ da metaclass é chamado e cria a nova classe
NOTA: O __new__ da classe cria e retorna uma nova instancia, da metaclass cria e retorna uma CLASSE
2. __call__ da metaclass é chamado com os argumentos e chama:
    a. __new__ da class com os argumentos (cria a instância)
    b. __init__ da class com os argumentos
3. __call__ da metaclass termina a execução

Métodos importantes da metaclass
__new__(mcs, name, bases, dict) (Cria a classe)
__call__(cls, *args, **kwargs) (Cria e inicializa a instância)

"Metaclasses são magias mais profundas do que 99% dos usuários deveriam se preocupar. Se você quer saber se precisa
delas, não precisa (as pessoas que realmente precisam delas sabem com certeza que precisam delas e não precisam de
uma explicação sobre o porquê)."
— Tim Peters (CPython Core Developer)

object acima
class Foo:
    ...
"""


class Foo:
    ...


f = Foo()
# f is an instance of Foo
print(isinstance(f, Foo))  # output: True

# f has the type of the class Foo
print(type(f))  # output: <class '__main__.Foo'>

# Foo has the type of the class type
print(type(Foo))  # output: <class 'type'>

print()

# It is also possible to create a class using type
# It is not necessary to use the paremeter (object,) nether {}
# But we are doing that just to know that these two parameters are default
# the second param '(object,)' means that Bar is extending from object
# the third param '{}' dict is the dict of the class
Bar = type('Bar', (object,), {})
b = Bar()
print(isinstance(b, Bar))  # output: True
print(type(b))  # output: <class '__main__.Bar'>
print(type(Bar))  # output: <class 'type'>
