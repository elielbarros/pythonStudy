"""
# English
Class Relation - Association

The Association between at least two classes inside the system.

The Association is the relation type more common between classes.

Generally we have Association when one class has an attribute that makes a reference to another class.

The Association will not specify how a class controls another class life cycle.

# Portuguese
Class Relation - Association

A associação entre pelo menos duas classes dentro do sistema.

A Associação é o tipo de relacao mais comum entre classes.

Geralmente temos Associação quando uma classe possui um atributo que faz referência a outra classe.

A Associação não especificará como uma classe controla o ciclo de vida de outra classe.

"""


class Writer:
    def __init__(self, name, tool):
        self.name = name
        self.tool = tool

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool

    def write(self):
        return f'{self.name} is writing using {self.tool.name}'


class Tool:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


pen = Tool('Pen')
writer = Writer('John', pen)
print(writer.write())
