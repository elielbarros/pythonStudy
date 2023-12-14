"""
# English
- Multiple Inheritance
- About Diamant problem
D(B, C) - C(A) - B(A) - A
           A
         /   \
        B     C
         \   /
           D

MRO order changes according to the order of classes that was extend by subclass. MRO will consider the class that
was extended before another.
Example:
D(B, C)
If B and C have the same method, and we create an instance from D and try to access the method from super,
then the method called first will be from B
If this order reverse, then the method called will be from C

# Portuguese
- Heranca Multipla
- Sobre o problema do diamante
D(B, C) - C(A) - B(A) - A
           A
         /   \
        B     C
         \   /
           D

A ordem do MRO muda de acordo com a ordem que eh feita a estensao de classe. MRO considera a classe que eh estendida
primeiro

Exemplo:
D(B, C)
Se B e C tiverem o mesmo método, e criarmos uma instância de D e tentarmos acessar o método de super, então o método chamado primeiro será de B
Se esta ordem for invertida, então o método chamado será de C
"""


class A:
    def show_class_name(self):
        print('A')


class B(A):
    def show_class_name(self):
        print('B')


class C(A):
    def show_class_name(self):
        print('C')


class D(B, C):
    def show_class_name(self):
        print('D')


d_ = D()
d_.show_class_name()
print(D.__mro__)
# output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
