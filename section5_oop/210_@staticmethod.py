"""
#English
@staticmethod are static methods accessible with no need to instantiate a class.

Static method does not need any argument.

Static method does not have access to 'self' or 'cls'.

# Portuguese
@staticmethod sao metodos estaticos acessiveis sem necessidade de instanciar a classe.

O metodo estatico tambem nao precisa ter nenhum argumento.

O metodo estatico nao tem acesso ao 'self' ou ao 'cls'.
"""


class CalcUtil:
    @staticmethod
    def sum_(a, b):
        print(a + b)

    @staticmethod
    def print_(*args, **kwargs):
        print(args, kwargs)


CalcUtil.sum_(1, 2)  # output: 3
CalcUtil.print_(1, 2, 3)  # output: (1, 2, 3) {}
CalcUtil.print_(named=1)  # output: () {'named': 1}
