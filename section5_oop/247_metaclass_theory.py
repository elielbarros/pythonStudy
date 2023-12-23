"""
# English


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
