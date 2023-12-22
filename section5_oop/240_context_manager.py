"""
# English
Context Manager with classes - Creating and Using context managers.
You can implement your own protocols just by implementing the dunder methods that Python will use.
This is called Duck typing, a concept related to dynamic typing where Python is not interested in
type, but if some methods exist in your object for it to work properly.
Duck Typing:
When I see a bird that walks like a duck, swims like a duck, and quacks like a duck, I call that bird a
duck.
To create a context manager, the __enter__ and __exit__ methods must be implemented.
The __exit__ method will receive the exception class, exception and traceback. If it returns True, exception in with
will be deleted.
Ex:
with open('aula149.txt', 'w') as arquivo:

# Portuguese
Context Manager com classes - Criando e Usando gerenciadores de contexto
Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o Python vai usar.
Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no
tipo, mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.
Duck Typing:
Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de
pato.
Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.
O método __exit__ receberá a classe de exceção, a exceção e o traceback. Se ele retornar True, exceção no with será
suprimidas.
Ex:
with open('aula149.txt', 'w') as arquivo:
"""


class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Open File')
        self._file = open(self.file_path, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Close File')
        self._file.close()


with MyOpen('240_class.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    print('WITH', file)
