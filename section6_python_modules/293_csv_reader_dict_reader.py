"""
# English
1. csv.reader
    - Read CSV in a list format

2. csv.DictReader
    - Read CSV in a dict format

# Portuguese
1. csv.reader
    - le o CSV em formato de lista

2. csv.DictReader
    - le o CSV em formato de dicionario
"""
import csv
from pathlib import Path

CSV_FILE_PATH = Path(__file__).parent / 'static' / 'class_293.csv'

with open(CSV_FILE_PATH, 'r') as file_:
    csv_reader = csv.reader(file_)

    for raw in csv_reader:
        print(raw)


with open(CSV_FILE_PATH, 'r') as file_:
    csv_dict_reader = csv.DictReader(file_)

    # How get column names
    # .fieldnames
    print(csv_dict_reader.fieldnames)
    for raw_dict in csv_dict_reader:
        print(raw_dict, type(raw_dict))
