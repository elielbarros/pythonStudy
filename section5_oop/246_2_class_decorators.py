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
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, function):
        def inner_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * self.multiplier

        return inner_function


@Multiply(10)
def sum_(x, y):
    return x + y


# What will happen
# When we call for method sum_ with params x and y, and a param inside Multiply class parentheses
# We must initialize class Multiply with extra param to receive the number we are sending.
# We must receive the function inside dunder call and make as we do with decorated function.
print(sum_(1, 2))  # output: 30
