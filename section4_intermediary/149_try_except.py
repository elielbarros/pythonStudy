"""
DOCUMENTATION: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
Try - Try to execute a code

Except - Catch except raised by try block

Finally - Will execute after try or except
"""

string_ = 'test'
a = 1
b = 0

try:
    convert = int(string_)
    result = a / b
except ZeroDivisionError as zeroDivisionError:
    print("Error", zeroDivisionError)
except ValueError as valueError:
    print("Error", valueError)
except Exception:
    print("Unknown error")


try:
    result = a / b
    convert = int(string_)
except (ZeroDivisionError, ValueError) as generalError:
    print("Error", generalError)
except Exception:
    print("Unknown error")

