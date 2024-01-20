"""
# English
- zipfile -

Provides tools for working with zip files.
With zip files, extract content from existing zip files and manipulate files within zip files.

# Portuguese
- zipfile -

Fornece ferramentas para trabalhar com arquivos zip.
Cria arquivos zip, extrai conteudo de arquivos zip existentes e manipula arquivos dentro de arquivos zip.
"""
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

ROOT_PATH = Path(__file__).parent
ZIP_DIRECTORY_PATH = ROOT_PATH / 'static' / 'class_304'
ZIP_FILE_PATH = ZIP_DIRECTORY_PATH / 'zipped_304.zip'
UNZIP_FILE_PATH = ZIP_DIRECTORY_PATH / 'unzipped_304'

shutil.rmtree(ZIP_DIRECTORY_PATH, ignore_errors=True)

ZIP_DIRECTORY_PATH.mkdir(exist_ok=True)


def create_files(quantity: int, zip_dir: Path):
    for i in range(quantity):
        text_file = f'file_{i}.txt'
        text_path = zip_dir / text_file
        with open(text_path, 'w') as file:
            file.write('Hello World!')


create_files(5, ZIP_DIRECTORY_PATH)

# Zipping the files
with ZipFile(ZIP_FILE_PATH, 'w') as zipf:
    for root, dirs, files in os.walk(ZIP_DIRECTORY_PATH):
        for file in files:
            # Se nao colocar o segundo parametro como o nome do arquivo
            # o zip.write vai escrever todas as pastas anteriores ao arquivo
            zipf.write(os.path.join(root, file), file)

# Read Zipped Files
with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
    for file_ in zipf.namelist():
        print(file_)

# Unzip Files
with ZipFile(ZIP_FILE_PATH, 'r') as zipf:
    zipf.extractall(UNZIP_FILE_PATH)
