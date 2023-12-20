"""
# English
Dunder means DOUBLE UNDERSCORE = __dunder__

Dunder makes a reference to Special Methods or Magic Methods

https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames

Comparison magic methods
__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other

Normal arithmetic operators
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other

Unary operators and functions
__neg__(self) - -self

Representing class
__str__(self) - str  Defines behavior for when str() is called on an instance of your class.
__repr__(self) - str repr() is intended to produce output that is mostly machine-readable (in many cases, it could be
valid Python code even), whereas str() is intended to be human-readable.

# Portuguese
Dunder significa duplo underscore = __dunder__

Dunder faz referencia a Metodos Especiais ou Metodos Magicos
"""


class Point:

    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # It is like a convention, use dunder str to describe what is inside class
    # NOTE: It will be called before dunder repr!
    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    # Define the class and your attributes
    # NOTE: If has dunder str already, it will return str. If it has not, it will call repr.
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        # It is possible to use !r or !s
        # !r will return the repr from the value type
        # !s will return the str from the value type
        return f'{class_name}({self.x!r}, {self.y!r}, {self.z!r})'

    # __add__ dunder is responsible for implement how two objects must be added
    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Point(sum_x, sum_y)

    # __gt__ dunder is responsible for validating if self is greater than other
    def __gt__(self, other):
        sum_self = self.x + self.y
        sum_other = other.x + other.y
        return sum_self > sum_other



if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = p1 + p2
    print(p3)  # output: 4, 6, String
    print(p1 > p2)  # output: False
