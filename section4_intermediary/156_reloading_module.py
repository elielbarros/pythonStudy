"""
When we import a module, Python will create an instance from this imported module.
This instance created is called Singleton.
That means that Python will create only ONE instance from this module and use it.
No matter how many times we import this module again, it will always be one instance.

But if we want to reload this module, we have to use importlib
"""
import importlib
import class_156_module_example

print(class_156_module_example)

for index in range(3):
    importlib.reload(class_156_module_example)
    print(index)

print('This is the end')
