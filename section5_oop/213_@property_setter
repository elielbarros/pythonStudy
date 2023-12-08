"""
# English
By convention, the attributes that starts with underline or twice underline are attributes that must not be used out
of class

To configure setter, we have to configure getter first.

After configure getter, we will use the annotation @getter_name.setter to configure the method defined as setter.

We will use the configured setter inside method __init__.

The attribute that maintain this information will be _color.

# Portuguese
Por convencao, atributos que comecam com underline ou duplo underline, sao atributos que nao devem ser usados fora da
classe.

Para configurar setter, temos que configurar o getter primeiro.

Apos configuracao do getter, usaremos a anotacao @nome_do_getter.setter para configurar o metodo definido como setter.

Usaremos o setter configurado, no metodo __init__.

O atributo que guarda a informacao serah _color.
"""


class Pen:
    def __init__(self, color):
        # Here we will use setter to define color
        self.color = color

    @property
    def color(self):
        print('GET COLOR')
        return self._color

    @color.setter
    def color(self, color):
        print(f'SET COLOR: {color}')
        if color:
            self._color = color
            return
        raise ValueError('You must provide a valid Color')


p = Pen('Orange')
print(p.color)

p.color = 'White'
print(p.color)
