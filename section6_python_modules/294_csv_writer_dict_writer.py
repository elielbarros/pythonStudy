"""
# English
1. csv.writer
    - Write values from a list of dict
2. csv.DictWriter
    - Write dict directly

# Portuguese
1. csv.writer
    - Escreve valores de uma lista de dicionario
2. csv.DictWriter
    - Escreve dicionario diretamente
"""
import csv
from pathlib import Path

CSV_FILE_PATH = Path(__file__).parent / 'static' / 'class_294.csv'

client_list = [
    {'name': 'john', 'age': '499', 'address': 'av asia'},
    {'name': 'mary', 'age': '300', 'address': 'av america'}
]

with open(CSV_FILE_PATH, 'w') as file_:
    column_name_list = client_list[0].keys()
    writer = csv.writer(file_)

    writer.writerow(column_name_list)

    for client in client_list:
        writer.writerow(client.values())

CSV_FILE_PATH.unlink()

with open(CSV_FILE_PATH, 'w') as file_:
    column_name_list = client_list[0].keys()
    dict_writer = csv.DictWriter(
            file_, fieldnames=column_name_list
    )

    dict_writer.writeheader()

    for client in client_list:
        dict_writer.writerow(client)


