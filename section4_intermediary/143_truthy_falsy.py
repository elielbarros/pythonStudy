"""
Truthy and Falsy values, mutable and immutable types

"Truthy" and "Falsy" are values considered True or False when used as boolean

Mutable - [] {} set()

Immutable - () "" 0 0.0 None False range(10)
"""

# Mutable
list_ = []
dictionary = {}
set_ = set()

# Immutable
tuple_ = ()
string_ = ''
integer_ = 0
float_ = 0.0
null_ = None
false_ = False
range_ = range(0)


def falsy_(value):
    return 'truthy' if value else 'falsy'


# Mutable experiment
print('Mutable experiment')
print(list_, falsy_(list_))  # output: [] falsy

print()

print(dictionary, falsy_(dictionary))  # output: {} falsy

print()

print(set_, falsy_(set_))  # output: set() falsy

print()

# Immutable experiment
print('Immutable experiment')
print(tuple_, falsy_(tuple_))  # output: () falsy

print()

print(f'{string_=}', falsy_(string_))  # output: string_='' falsy

print()

print(integer_, falsy_(integer_))  # output: 0 falsy

print()

print(float_, falsy_(float_))  # output: 0.0 falsy

print()

print(null_, falsy_(null_))  # output: None falsy

print()

print(false_, falsy_(false_))  # output: False falsy

print()

print(range_, falsy_(range_))  # output: range(0, 0) falsy
