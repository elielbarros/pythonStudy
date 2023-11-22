# To import from package, we have to do:
# from class_157_package.class_157_module_example import sum_
# print(sum_(1, 3))  # output: 4

# Another way to import from package:
# import class_157_package.class_157_module_example
# print(class_157_package.class_157_module_example.sum_(1, 3))  # output: 4

# Another way to import module from package:
from section4_intermediary.class_159_package import class_157_module_example
print(class_157_module_example.sum_(1, 3))  # output: 4

# Another way is bad practice but also possible
# We could also include __all__ to include all methods we want from module.
# But to do that, we have to go on module and turn it explict.
# So it will be possible to access variable but not possible to access the method sum_
# because we did not put it on __all__
print(variable)

