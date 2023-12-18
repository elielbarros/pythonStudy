"""
# English

To create an exception with Python, it is necessary to inherit from any language exception.

The recommendation is to inherit from Exception class.

Documentation:
https://docs.python.org/3/library/exceptions.html

It is good practice use 'Error' as the final Word custom exception class created.

# Portuguese

Para criar uma excecao com Python, eh necessario herdar de qualquer excessao da linguagem.

A recomendacao eh herdar da classe Exception.

Documentacao:
https://docs.python.org/3/library/exceptions.html

Eh bom seguir a convencao de colocar ao fim da excecao criada, a palavra 'Error'.
"""


class MyError(Exception):
    ...
