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


class AnotherError(Exception):
    def raise_exception(self):
        raise AnotherError('Hello World Another Exception')


my_error = MyError()
# my_error.raise_exception()  # output: MyError: Hello World Exception

# To treat exception with Python, it is necessary to use Try Except
try:
    my_error.raise_exception()
except (MyError, ZeroDivisionError) as error:
    print(error)  # output: Hello World Exception
    # It is possible to print Error Class Name
    print(error.__class__.__name__)  # output: MyError
    # It is also possible to raise again this error with different phrase
    another_exception = AnotherError('Hello World Another Exception')
    raise another_exception from error  # output: The above exception was the direct cause of the following exception:
                                                # AnotherError: Hello World Another Exception
