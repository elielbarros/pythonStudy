"""
# English
json.dump(movie_dict, file_, indent=2, ensure_ascii=False)
movie_dict - python dictionary
file_ - file opened with builtin.open() using the 'with' statement
indent - guarantees the indentation of the dictionary as json in the file
ensure_ascii - ensures a file format as ascii

# Portuguese
json.dump(movie_dict, file_, indent=2, ensure_ascii=False)
movie_dict - dicionario python
file_ - arquivo aberto com builtin.open() usando o statement 'with'
indent - garante a identacao do dicionario como json no arquivo
ensure_ascii - garante formato do arquivo como ascii

"""

import json
import os

FILE_NAME = 'class_290.json'
FILE_ABSOLUT_PATH = os.path.abspath(
        os.path.join(
                os.path.dirname(__file__),
                FILE_NAME
        )
)

print(os.path.dirname(__file__))  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules
print(FILE_ABSOLUT_PATH)  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules/class_290.json

movie_dict = {
    'title': 'O Senhor dos Aneis: A sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(FILE_ABSOLUT_PATH, 'w') as file_:
    json.dump(movie_dict, file_, indent=2, ensure_ascii=False)


with open(FILE_ABSOLUT_PATH, 'r') as file_:
    movie_loaded_as_dict = json.load(file_)
    print(movie_loaded_as_dict)
