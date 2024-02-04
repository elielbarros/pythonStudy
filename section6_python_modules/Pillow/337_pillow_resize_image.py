"""
# English
Pillow is a Python image processing library that offers an easy-to-use interface for performing various operations on
images. It is a fork of the PIL (Python Imaging Library) project and is actively maintained, offering support for
Python 2 and Python 3.

# Portuguese
Pillow é uma biblioteca de processamento de imagens em Python que oferece uma interface fácil de usar para realizar
várias operações em imagens. Ela é uma bifurcação (fork) do projeto PIL (Python Imaging Library) e é mantida
ativamente, oferecendo suporte a Python 2 e Python 3.

Como usar Pillow?
    - pip install pillow
"""
from pathlib import Path

from PIL import Image

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
ORIGINAL_FILE_PATH = STATIC_PATH / 'original.JPG'
NEW_FILE_PATH = STATIC_PATH / 'new.JPG'

pil_image = Image.open(ORIGINAL_FILE_PATH)

# RESIZING IMAGE
print(pil_image.size)  # output: (4898, 3265)

# GETTING WIDTH AND HEIGHT FROM ORIGINAL IMAGE FILE
width, height = pil_image.size

# GETTING ORIGINAL IMAGE FILE DETAILED INFORMATION
exif = pil_image.info['exif']

# TO RESIZE IMAGE MAINTAINING THE PROPORTION CHOOSE CHANGE HEIGHT OR WIDTH
# width     new_width
# height    ??
new_width = 640
new_height = round(height * new_width / width)

print(new_width, new_height)  # output: 640 427

# RESIZING IMAGE
new_image = pil_image.resize(size=(new_width, new_height))

# SAVING IMAGE RESIZED
new_image.save(
        NEW_FILE_PATH,
        optimize=True,
        quality=70,
        exif=exif
)
