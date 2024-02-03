"""
# English

# Portuguese
"""

from pathlib import Path

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

writer = PdfWriter()
writer.add_page(page0)

with open(DEST_PATH / 'page0.pdf', 'wb') as file:
    writer.write(file)

writer = PdfWriter()
with open(DEST_PATH / 'all_pages.pdf', 'wb') as file:
    for page in pages:
        writer.add_page(page)
    writer.write(file)


for index, page in enumerate(pages):
    writer = PdfWriter()
    file_name = f'all_pages{index}.pdf'
    with open(DEST_PATH / file_name, 'wb') as file:
        writer.add_page(page)
        writer.write(file)
