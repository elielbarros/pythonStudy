"""
# English
__new__ and __init__

new and init dunder has the same objective, initialize a class instance.

difference:
__new__ will create and return created class initialized, so new use cls.
__init__ will get instance self and initialize class.


# Portuguese
__new__ e __init__

new e init dundere tem o mesmo objetivo, inicializar uma instancia da classe.

diferencas:
__new__ vai criar e retornar a classe criada e inicializada, com isso ele usa cls.
__init__ vai pegar a instancia da classe ja criada, self e inicializar a classe.
"""


class Foo:
    def __init__(self, x):
        self.x = x

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


instance = Foo(1)
print(instance.x)  # output: 1
