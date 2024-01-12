import math
import os
from itertools import count


def size_format(bytes_size: int, base: int = 1024) -> str:
    if bytes_size <= 0:
        return '0B'

    size_abbreviation_tuple = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    size_abbreviation_index = int(math.log(bytes_size, base))

    pow_ = base ** size_abbreviation_index

    final_size = round(bytes_size / pow_, 2)

    size_abbreviation = size_abbreviation_tuple[size_abbreviation_index]

    return f'{final_size} {size_abbreviation}'


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
        file_path = os.path.join(root, file_)
        file_size = size_format(os.path.getsize(file_path))  # os.path.getsize and stats.st_size are the same!

        stats = os.stat(file_path)
        size = stats.st_size

        print(f'\t\t{counter_} Actual File {file_} Size {size}')
