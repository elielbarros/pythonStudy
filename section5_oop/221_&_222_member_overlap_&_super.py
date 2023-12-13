"""
# English
In Python, following the concept of 'Method Resolution Order', we can create methods and properties identical to those
of the superclass in the subclass. Therefore, if we access a property or use a method that exists in both classes,
the first one to be invoked will be that of the subclass.

We can use this to perform two actions inside the child class and then in the superclass using 'super()'

When there are multiple inheritances, and we want to access a specific method of one of the superior classes to the
subclass in question, we can use 'super(class_&_point_of_view, self).method_()'

# Portuguese
Em Python, seguindo o conceito de 'Method Resolution Order', podemos criar metodos e propriedades identicas as da super
classe na subclasse. Com isso, se acessarmos uma propriedade ou usarmos um metodo que existe nas duas classes,
o primeiro a ser invocado serah o da subclasse.

Nos podemos executar usar isso para executar duas acoes dentro da classe filha e depois na classe super usando 'super()'

Quando houver multiplas herancas e quisermos acessar um metodo especifico de uma das classes superior a subclasse em
questao podemos usar 'super(classe_e_ponto_de_vista_de_execucao, self).metodo_a_executar()'
"""


class MyString(str):
    def upper(self):
        print('Execute Something Here')
        return super().upper()


string_ = MyString('John')
print(string_)  # output: John
print(string_.upper())


# output:
# Execute Something Here
# JOHN

class A:
    property_a = 'value A'

    def __init__(self, attribute_):
        self.attribute_ = attribute_

    def method_(self):
        print(self.property_a)


class B(A):
    property_b = 'value B'

    def __init__(self, attribute_, another_attribute):
        super().__init__(attribute_)
        self.another_attribute = another_attribute

    def method_(self):
        print(self.property_b)


class C(B):
    property_c = 'value C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Hello World')

    def method_(self):
        super(B, self).method_()
        super(C, self).method_()
        print(self.property_c)


c_ = C('first', 'thing')
c_.method_()
# output:
# value A
# value B
# value C

print(c_.attribute_)  # output: first
print(c_.another_attribute)  # output: thing
