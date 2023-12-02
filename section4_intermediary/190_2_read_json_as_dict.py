"""
json

# English
How to convert Python dict into json and save it on file.
The method .dump() is responsible for saving the dictionary as json and write on file.

Example: json.dump(dictionary_here, file_path_here)

It is possible to define if

# Portuguese
Como converter um dicionario Python em json e salva-lo em um arquivo.
O metodo .dump() da biblioteca json eh responsavel por salvar o dicionario como json e escrever no arquivo.

Exemplo: json.dump(dicionario_aqui, caminho_arquivo_aqui)

"""
import json

file_path = '190_class.json'

with open(file_path, 'r') as file:
    person = json.load(file)
    print(person)
    print(type(person))
