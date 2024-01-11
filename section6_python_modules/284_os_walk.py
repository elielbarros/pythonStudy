import os
from itertools import count

path = os.path.join('/home', 'eliel', 'Documents', 'projects', 'pythonStudy', 'section6_python_modules')
all_files = []
counter = count()
counter_ = 0
for root, dirs, files in os.walk(path):
    counter_ = next(counter)
    print(f'{counter_} Actual Root {root}')

    for dir_ in dirs:
        print(f'\t{counter_} Actual Dir {dir_}')

    files = sorted(files)
    for file_ in files:
        print(f'\t\t{counter_} Actual File {file_}')
