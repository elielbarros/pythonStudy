"""
Packages could be initialized with __init__ package

Anything that we initialize on __init__ inside package... when imported by another module
will already execute what is inside __init__

If we import module inside init, then module_b and module_c will be available
"""

from class_159_package import sum_
from class_159_package import subtract_

print(sum_(1, 2))

print(subtract_(2, 1))
