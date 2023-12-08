"""
# English
The decorator @property in Python is used to convert a class method into a property.
It allow access to a method as attribute, with no need to explicitly call the method.

@property will be used in the following situations:
- used as getter
- to avoid broke client code
- to enable setter
- to perform actions when obtaining an attribute

# Portuguese
O decorator @property no Python é utilizado para transformar um metodo de uma classe em uma propriedade.
Ele permite que voce acesse o metodo como se fosse um atributo, sem a necessidade de chamar explicitamente o metodo.

@property serah usado nas seguintes situacoes:
- usado como getter
- para evitar quebrar codigo do cliente
- para habilitar setter
- para executar acoes ao obter um atributo
"""


class Pen:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        print('GET COLOR')
        return self._color


p = Pen('Orange')
print(p.color)
