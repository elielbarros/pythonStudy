"""
Ternary Operation
Will check if a condition is True or false and return a value related to the condition
"""

condition = 0 == 0
value_for_condition_true = 'Value for condition true'
value_for_condition_false = 'Value for condition false'
variable = value_for_condition_true if condition else value_for_condition_false

print(variable)

condition = 0 == 1
variable = value_for_condition_true if condition else value_for_condition_false
print(variable)

# It is possible do two Ternary Operation at the same time
condition_false = 0 == 1
condition_true = 0 == 0
value_for_true_1 = 'Value for True 1'
value_for_false_true = 'Value for False True'
value_for_false_2 = 'Value for False 2'
variable_1 = value_for_true_1 if condition_true else value_for_false_true if condition_false else value_for_false_2
variable_2 = value_for_true_1 if condition_false else value_for_false_true if condition_true else value_for_false_2
variable_3 = value_for_true_1 if condition_false else value_for_false_true if condition_false else value_for_false_2
print(variable_1)
print(variable_2)
print(variable_3)
