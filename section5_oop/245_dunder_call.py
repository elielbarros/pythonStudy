"""
# English
Dunder __call__
Callable is something that could be executed with parentheses
In Normal Classes, __call__ create an instance of a class 'callable'.

# Portuguese
Metodo especial __call__
Callable eh algo que pode ser executado com parenteses
Em classes normais, __call__ faz a instancia de uma classe 'callable'.
"""


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'is calling', self.phone)


call = CallMe('11111111111')
call('John')  # output: John is calling 11111111111
