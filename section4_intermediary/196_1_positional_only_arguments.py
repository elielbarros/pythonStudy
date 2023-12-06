"""
# English

PEP 570 - Python Positional-Only Parameters
https://peps.python.org/pep-0570/

Define that the method will accept ONLY POSITIONAL PARAMETERS

How does that?

Using '/' as parameter

NOTE: Everything coming before slash '/' cannot be NAMED ARGUMENT. Everything after slash '/' could be NAMED ARGUMENT.

Look example below

# Portuguese

PEP 570 - Python Positional-Only Parameters
https://peps.python.org/pep-0570/

Define que o método aceitará APENAS PARÂMETROS POSICIONAIS

Como é que isso?

Usando '/' como parâmetro

NOTA: Tudo o que vem antes da barra '/' não pode ser NOMEADO ARGUMENTO. Tudo após a barra '/' pode ser NOMEADO
ARGUMENTO.

Veja exemplo abaixo
"""


def sum_(a, b, /):
    print(a + b)


# it is possible to send positional parameters ONLY
sum_(1, 2)  # output: 3


# But if we try to pass named argument, it will raise exception:
# sum_(a=1, b=2)  # output: TypeError: sum_() got some positional-only arguments passed as keyword arguments: 'a, b'

# Another important information is that, arguments after '/' (slash) could be used as named argument
# See the example below
def subtraction(a, b, /, x, y):
    return a - b - x - y


print(subtraction(1, 2, x=3, y=4))  # output: -8
