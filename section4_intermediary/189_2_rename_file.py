"""
os

# English
How rename file using the library 'os'

The method rename() is responsible for that: os.rename(file_path, 'new_name.txt')

# Portuguese
Como renomear arquivo usando a biblioteca 'os'

O metodo rename() eh responsavel por isso: os.rename(file_path, 'novo_nome.txt')
"""

import os

file_path = '189_class.txt'


def create_file():
    with open(file_path, 'w'):
        pass


create_file()

os.rename(file_path, '189_class_new_name.txt')

