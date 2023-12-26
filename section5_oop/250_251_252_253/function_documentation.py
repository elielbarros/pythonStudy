"""
Function Documentation

This module contains function and documentation about the function.
"""


# This is the old documentation
def sum_(x, y):
    """
    The function sum_ will receive two params x and y and sum these params.

    :param x: Number 1
    :type x: int or float
    :param y: Number 2
    :type y: int or float

    :return: The result of x + y
    :rtype: int or float
    """
    return x + y


def sum__(x: int | float, y: int | float) -> int | float:
    """
    The function sum__ will receive two params (x, y) and sum it.

    This method will not have old documentation.
    """
    return x + y
