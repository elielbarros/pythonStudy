"""
# English
How to read a pdf with PdfReader?
     Use PdfReader(file path here)

How to show the number of pages the PDF has?
     reader.pages

How to extract text from pdf?
     1. pages = reader.pages
     2. page0 = pages[0]
     3. page0.extract_text()

How to extract images from PDF?
     1. pages = reader.pages
     2. page0 = pages[0]
     3. page0.images

How to extract the title of an image from PDF?
     1. pages = reader.pages
     2. page0 = pages[0]
     3. page0.images
     4. image0 = page0.images[0]
     5. title = image0.name

How to extract image from pdf?
     1. pages = reader.pages
     2. page0 = pages[0]
     3. page0.images
     4. image0 = page0.images[0]
     5. image_data = image0.data

# Portuguese
Como ler um pdf com PdfReader?
    Use PdfReader(caminho do arquivo aqui)

Como mostrar o numero de paginas que o pdf tem?
    reader.pages

Como extrair o texto do pdf?
    1. pages = reader.pages
    2. page0 = pages[0]
    3. page0.extract_text()

Como extrair as imagens do pdf?
    1. pages = reader.pages
    2. page0 = pages[0]
    3. page0.images

Como extrair o titulo de uma imagem do pdf?
    1. pages = reader.pages
    2. page0 = pages[0]
    3. page0.images
    4. image0 = page0.images[0]
    5. title = image0.name

Como extrair a imagem do pdf?
    1. pages = reader.pages
    2. page0 = pages[0]
    3. page0.images
    4. image0 = page0.images[0]
    5. image_data = image0.data
"""

from pathlib import Path

from PyPDF2 import PdfReader

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
DEST_PATH = STATIC_PATH / 'dest'
REPORT_BACEN_FILE_PATH = STATIC_PATH / 'relatorio-focus.pdf'

DEST_PATH.mkdir(exist_ok=True)

reader = PdfReader(REPORT_BACEN_FILE_PATH)

print(len(reader.pages))  # output: 2

pages = reader.pages

for page in pages:
    print(page)

first_page = pages[0]

extracted_text_first_page = first_page.extract_text()
print(extracted_text_first_page)

extracted_images_first_page = first_page.images
print(extracted_images_first_page)

with open(DEST_PATH / extracted_images_first_page[0].name, 'wb') as image_file:
    image_file.write(extracted_images_first_page[0].data)
