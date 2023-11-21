"""
DOCUMENTATION: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
Try - Try to execute a code

Except - Catch except raised by try block

Finally - Will execute after try or except
"""
a = 1
b = 0

try:
    result = a / b
except (ZeroDivisionError, ValueError) as generalError:
    # It is possible to get the class name error
    print('Class Error Name:', generalError.__class__.__name__)
    print('Error:', generalError)
except Exception:
    print('Unknown error')
