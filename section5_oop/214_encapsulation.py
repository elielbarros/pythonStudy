"""
# English
Encapsulation - Encapsulation is the process of grouping functions and data into a single entity.
To access these data members, the member function’s scope must be set to “public,” while the data members’ scope must
be set to “private.”
Available Access Modifiers: public, protected and private

In Python we do not have these Access Modifiers but by convention we use data:
- Without Underline: Means that data is public and could be used anywhere
- With one Underline (single leading underscore): Means that data is protected and could be used inside your own
class and subclasses
- With two Underline (double leading underscore): Means that data is private and could be used only inside your own
class. "name mangling"

"Name Mangling" means that to access methods with double leading underscore, will be like
instance._ClassName__private_method()

# Portuguese
Encapsulamento - Encapsulamento é o processo de agrupar funções e dados em uma única entidade.
Para acessar esses membros de dados, o escopo da função membro deve ser definido como “público”, enquanto o escopo
dos membros de dados deve ser definido como “privado”.
Modificadores de acesso disponíveis: público, protegido e privado

Em Python não temos esses modificadores de acesso, mas por convenção usamos dados:
- Sem underline: significa que os dados são públicos e podem ser usados em qualquer lugar
- Com um underline (underline único): significa que os dados sao protegidos e podem ser usados dentro de sua própria
classe e subclasses
- Com dois underline (underline duplo): significa que os dados são privados e podem ser usados apenas dentro da
sua própria classe. "Name Mangling"

"Name Mangling" significa que para acessar metodos com sublinhado duplo, será como
instance._ClassName__private_method()
"""


class Foo:
    def __init__(self):
        self.public = 'public variable'
        self._protected = 'protected variable'
        self.__private = 'private variable'

    def public_method(self):
        print(self._protected_method())
        return 'public method'

    def _protected_method(self):
        print(self.__private_method())
        return 'protected method'

    def __private_method(self):
        print(self.__private)
        return 'private method'


f = Foo()
print(f.public_method())
print()
print(f._Foo__private_method())  # It is not correct but it is accessible
