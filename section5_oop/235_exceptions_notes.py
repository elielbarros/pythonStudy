"""
# English

To create an exception with Python, it is necessary to inherit from any language exception.

The recommendation is to inherit from Exception class.

Documentation:
https://docs.python.org/3/library/exceptions.html

It is good practice use 'Error' as the final Word custom exception class created.

Is used 'raise' to throw an exception with Python.

# Portuguese

Para criar uma excecao com Python, eh necessario herdar de qualquer excessao da linguagem.

A recomendacao eh herdar da classe Exception.

Documentacao:
https://docs.python.org/3/library/exceptions.html

Eh bom seguir a convencao de colocar ao fim da excecao criada, a palavra 'Error'.

Em Python eh usado 'raise' para 'levantar' uma excecao.
"""


class MyError(Exception):
    def raise_exception(self):
        raise MyError('Hello World Exception')


my_error = MyError()

try:
    my_error.raise_exception()
except MyError as error:
    another_error = MyError()
    # it is possible to add NOTES into exception using the method available add_note()
    another_error.add_note('This exception is an example!')
    error.add_note('Hello Error Note')
    # We can copy error notes from error too
    another_error.__notes__ += error.__notes__.copy()  # output: Hello Error Note
    raise another_error from error  # output: This exception is an example!
