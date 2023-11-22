"""
Understanding your own module Python

The first module executed is called __main__

You can import another module in your complete way or 'object from complete way'

Python knows where __main__ module is and the others below it

Python does not recognize the folder and module above __main__ for default

Python knows all modules and patch that are present on the sys.path path
"""
import sys

import module_example_class_154

# We cant import exercise0 because it is in another patch as module
# import exercise0

# We can import any file on the same directory that this module is
# import atest

print("This module is called:", __name__)
print(*sys.path, sep='\n')

print()

# We can include a directory to sys path and python will understand this import
sys.path.append('/home/eliel/Documents/projects/pythonStudy/section3_basic')
print(*sys.path, sep='\n')
import arithmeticOperation

