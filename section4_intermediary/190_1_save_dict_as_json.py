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

person = {
    'name': 'John',
    'last_name': 'Doe',
    'address': [
        {'street': 's1', 'number': 32},
        {'street': 's2', 'number': 55}
    ],
    'height': 1.8,
    'preferred_number': (2, 4, 6, 8, 10),
    'dev': True,
    'nothing': None
}

with open('190_class.json', 'w') as file:
    # It is possible to set ascii False
    # It is also possible to ident file
    json.dump(person, file, ensure_ascii=False, indent=2)
