"""
# English

PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/

Define where will end Positional Arguments. After that, we will have at least one NAMED ARGUMENT.

To define it, we will use '*' to denote this limit.

Before '*' everything must be Positional Argument or Named Argument.

After '*' everything MUST BE Named Argument.

If we want to use only Positional Argument before '*' is just use '/' too.

Look example below

# Portuguese

PEP 3102 – Keyword-Only Arguments
https://peps.python.org/pep-3102/

Define ateh onde os Argumentos Posicionais podem ser usados. Apos isso, nos teremos, pelo menos um Argumento Nomeado.

Para definir isso, nos temos que usar '*' para denotar esse limite.

Antes de '*' tudo precisa ser Argumento Posicional ou Argumento Nomeado.

Depois de '*' tudo PRECISA ser Argumento Nomeado.

Se quisermos usar apenas o argumento posicional antes de '*', basta usar '/' também.

Olhe o exemplo abaixo

"""


def sum_(a, b, *, c):
    print(a + b + c)


# sum_(1, 2, 3)  # output: TypeError: sum_() takes 2 positional arguments but 3 were given
sum_(1, 2, c=3)  # output: 6
sum_(1, b=2, c=3)  # output: 6


def sub_(a, b, /, *, c):
    print(a - b - c)


sub_(1, 2, c=3)  # output: -4
# sub_(1, b=2, c=3) TypeError: subtraction_() got some positional-only arguments passed as keyword arguments: 'b'
