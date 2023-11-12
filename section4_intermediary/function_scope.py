"""
Python Function Scope

Context in which the variables and parameters of a programming function are defined and can be accessed.

Exists two function scopes:
1. Global Scope
2. Local Scope
"""

global_scope_value = 10
global_scope_value_1 = 11


def make_print():
    # When define the global scope value here, it will be another variable different from the global that is outside
    global_scope_value = 2
    print(f'{global_scope_value=}')  # Global scope could be used inside function
    # It is possible to define global_scope_value as Global and change the value outside too
    global global_scope_value_1
    global_scope_value_1 = 13
    print(f'{global_scope_value_1=}')

    local_scope_value = 5  # But this local scope value could not be used outside this function
    print(f'Local Scope Value: {local_scope_value}')
    # NameError: name 'another_global_scope_value_defined_after_call_function' is not defined
    # print(another_global_scope_value_defined_after_call_function)


print(f'{global_scope_value_1=}')
print(f'{global_scope_value=}')
make_print()
print(f'{global_scope_value=}')

# print(local_scope_value)  # NameError: name 'local_scope_value' is not defined.

# This global value only will work if a make_print() after define it
another_global_scope_value_defined_after_call_function = 1

print(f'{global_scope_value_1=}')
