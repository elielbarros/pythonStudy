"""
Logical Operator 'IN'

When something of type A is 'IN' a group of something of Type A will return True
A = 1
Group(A) = 0,1,2,3,4,5

Logical Operator 'NOT IN'
When something of type A is 'NOT IN' a group of something of Type B will return True
A = 1
Group(B) = a,b,c,d,e,f
"""
group_a = [0, 1, 2, 3, 4, 5]
group_b = ['a', 'b', 'c', 'd', 'e', 'f']

print(1 in group_a)

print(1 in group_b)

print(1 not in group_b)

print('a' in group_a)

print('a' in group_b)

print('a' not in group_a)

#  0  1  2  3
#  J  O  H  N
# -4 -3 -2 -1
name = 'JOHN'
print(name[1])  # IT WILL RETURN O
print(name[-3])  # IT WILL RETURN O

print(name not in group_b)
