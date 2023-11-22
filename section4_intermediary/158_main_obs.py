"""
1. /actual/module_a.py
2. /actual/directory/module_b.py
3. /actual/directory/module_c.py

In case that module_b import module_c and module_a try to import module_b, then it will raise an exception
Because what __main__ from module_b could access is different from what __main__ from module_a could access.
"""

# So if we have module_b and module_c and module_b is importing module_c
# When we try to import module_b, we will have an exception
import class_157_package.class_158_module_b as module_b

module_b.subtract_(2, 1)  # output: ModuleNotFoundError: No module named 'class_158_module_c'

# To resolve it, we need to import as we are importing from here.
# Soh we have to import in module_b considering the package, and we will have access to module_c correctly
# from class_157_package.class_158_module_c import subtract_
# The problem is that if we try to execute module_b we will get an error, because module_b can not access package