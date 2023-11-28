"""
# English
group by - Group information considering a key.
Data must be ordered to be grouped.

# Portuguese
group by - Agrupar informacao considerando uma chave.
Os dados precisam estar ordenados para serem agrupados.
"""
from itertools import groupby

letters = ['a', 'a', 'b', 'c', 'a']

for key, group in groupby(sorted(letters)):
    print(f'{key=}')
    print(f'{list(group)=}')

# output:
# key='a'
# list(group)=['a', 'a', 'a']
# key='b'
# list(group)=['b']
# key='c'
# list(group)=['c']

print()

students = [
    {'name': 'Sydney', 'grade': 'A'},
    {'name': 'Safa', 'grade': 'B'},
    {'name': 'Saoirse', 'grade': 'A'},
    {'name': 'Byron', 'grade': 'C'},
    {'name': 'Finnian', 'grade': 'D'},
    {'name': 'Trinity', 'grade': 'A'},
    {'name': 'Elissa', 'grade': 'B'},
    {'name': 'Louise', 'grade': 'A'},
    {'name': 'Jasper', 'grade': 'C'},
    {'name': 'Cyrus', 'grade': 'D'},
]


def order_by_grade(student):
    return student['grade']


sorted_students = sorted(students, key=order_by_grade)

print(*sorted_students, sep='\n')

print()

for key, group in groupby(sorted_students, key=order_by_grade):
    print(f'{key=}')
    for item in group:
        print(item)
# output:
# key='A'
# {'name': 'Sydney', 'grade': 'A'}
# {'name': 'Saoirse', 'grade': 'A'}
# {'name': 'Trinity', 'grade': 'A'}
# {'name': 'Louise', 'grade': 'A'}
# key='B'
# {'name': 'Safa', 'grade': 'B'}
# {'name': 'Elissa', 'grade': 'B'}
# key='C'
# {'name': 'Byron', 'grade': 'C'}
# {'name': 'Jasper', 'grade': 'C'}
# key='D'
# {'name': 'Finnian', 'grade': 'D'}
# {'name': 'Cyrus', 'grade': 'D'}
