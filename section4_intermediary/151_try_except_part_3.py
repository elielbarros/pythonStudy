"""
DOCUMENTATION: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
Try - Try to execute a code

Except - Catch except raised by try block

Finally - Will always be executed after try or except

When use finally:
    - When open a file to do something and get an error
    - The file is open yet, but we have to close this connection
    - So we have to use finally to close it

When use else:
    - Use else when you want to do something after try without a raised error.

"""

try:
    print('Open File')
    8 / 0
except:
    print('Error opening file')
finally:
    print('Close file')

print()

try:
    print('Open File')
except (ZeroDivisionError, ValueError) as generalError:
    print('Error opening file')
except Exception as e:
    print('Unknown error')
else:
    print('File written correctly')
finally:
    print('Close file')