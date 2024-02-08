from PySide6.QtWidgets import QPushButton

from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;')

        # Change font with this way will avoid overwrite another configurations about font
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(45, 45)
        # self.setProperty('cssClass', 'specialButton')

