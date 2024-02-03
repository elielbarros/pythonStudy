"""
# English
How to use PdfMerger?

1. Import library
     - from PyPDF2 import PdfMerger
2. Define path of files that will be merged
     - files = [DEST_PATH/'page0.pdf', DEST_PATH/'page1.pdf']
3. Define path where the merged file will be saved
     - DEST_PATH/'merged_files.pdf'
4. Use PdfMerger's .append method to insert the pages that will be merged
     - for file in files:
         merger.append(file)
5. Use contextManager to create the file with merger
     - with open(DEST_PATH / 'merged_files.pdf', 'wb') as file:
         merger.write(file)

# Portuguese
Como usar o PdfMerger ?

1. Importar biblioteca
    - from PyPDF2 import PdfMerger
2. Definir caminho de arquivos que serao mesclados
    - files = [DEST_PATH / 'page0.pdf', DEST_PATH / 'page1.pdf']
3. Definir caminho onde o arquivo mesclado sera salvo
    - DEST_PATH / 'merged_files.pdf'
4. Usar o metodo .append do PdfMerger para inserir as paginas que serao mergeadas
    - for file in files:
        merger.append(file)
5. Usar contexManager para criar o arquivo com o merger
    - with open(DEST_PATH / 'merged_files.pdf', 'wb') as file:
        merger.write(file)
"""

from pathlib import Path

from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
DEST_PATH = STATIC_PATH / 'dest'
REPORT_BACEN_FILE_PATH = STATIC_PATH / 'relatorio-focus.pdf'

DEST_PATH.mkdir(exist_ok=True)

reader = PdfReader(REPORT_BACEN_FILE_PATH)

pages = reader.pages

page0 = pages[0]

for index, page in enumerate(pages):
    writer = PdfWriter()
    file_name = f'page{index}.pdf'
    with open(DEST_PATH / file_name, 'wb') as file:
        writer.add_page(page)
        writer.write(file)

files = [DEST_PATH / 'page0.pdf', DEST_PATH / 'page1.pdf']

merger = PdfMerger()
for file in files:
    merger.append(file)

with open(DEST_PATH / 'merged_files.pdf', 'wb') as file:
    merger.write(file)
