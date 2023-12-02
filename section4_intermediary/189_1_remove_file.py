"""
'os'

# English
How remove an existent file using 'os'

We could use two different methods from 'os'
- os.unlink(file_path)
- os.remove(file_path)

# Portuguese
Como remover um arquivo existente usando 'os'

Nos podemos usar dois metodos diferentes da biblioteca 'os'
- os.unlink(file_path)
- os.remove(file_path)

"""

import os

file_path = '189_class.txt'


def create_file():
    with open(file_path, 'w'):
        pass


create_file()

# We have os.unlink(file_path) method to remove file
os.unlink(file_path)

create_file()

# We also have os.remove(file_path) method to remove file
os.remove(file_path)
