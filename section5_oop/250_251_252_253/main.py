import class_documentation
import function_documentation
import many_lines
import one_line

# Using 'dir' it is possible to see everything that is inside one_line
# dir return a list of strings
print(dir(one_line))
# output: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# It is possible to print dunder doc from one_line
print(one_line.__doc__)  # output: Module documentation

# It is possible to print the path to the file
print(one_line.__file__)  # output: /home/eliel/Documents/projects/pythonStudy/section5_oop/250_251_252_253/one_line.py

# It is possible to print the module name
print(one_line.__name__)  # output: one_line

# Using the method 'help' it is possible to see what is inside the module one_line
help(one_line)

# This is a docstring with many lines
help(many_lines)

# This is a docstring with function documentation
help(function_documentation)

function_documentation.sum_(1, 2)

function_documentation.sum__(1, 2)

# This is a docstring with class documentation
help(class_documentation)

f = class_documentation.Foo()
f.bar()
