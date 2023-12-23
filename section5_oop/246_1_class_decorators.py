"""
# English
Class Decorators

Encapsulates and wraps a class with another class that adds or modifies behaviors. This is generally done using the
composition techinique, where a new class is created to wrap the original class.

# Portuguese
Classe Decoradora

Encapsula e envolve uma classe com outra clase que adicioona ou modifica comportamentos. Isso eh geralmente feito
usando a tecnica de composicao, onde uma nova classe eh criada para envolver a classe original.
"""


class Multiply:
    def __init__(self, function):
        print('INIT')
        self.function = function
        self.multiplier = 10

    def __call__(self, *args, **kwargs):
        print('CALLABLE')
        result = self.function(*args, **kwargs)
        return result * self.multiplier


@Multiply
def sum_(x, y):
    return x + y


# What will happen
# When we call for method sum_ with params x and y, Python will try to initialize class Multiply
# To initialize class Multiply, without an error:
# We must initialize the class with an extra argument, that will represent function
# We must implement dunder __call__ receiving arguments from the method sum_
# After receive function and your respective arguments we can calculate value as we want
print(sum_(1, 2))  # output: 30
