from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

from display import Display
from utils import isNumOrDot
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
        # self.setCheckable(True)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                if buttonText == '0':
                    button = Button(buttonText)
                    if not isNumOrDot(buttonText):
                        button.setProperty('cssClass', 'specialButton')
                    self.addWidget(button, i, j, 1, 2)

                    j += 1
                    nextButtonText = row[j]
                    button = Button(nextButtonText)
                    if not isNumOrDot(nextButtonText):
                        button.setProperty('cssClass', 'specialButton')
                    self.addWidget(button, i, 2, 1, 1)

                    j += 1
                    nextButtonText = row[j]
                    button = Button(nextButtonText)
                    if not isNumOrDot(nextButtonText):
                        button.setProperty('cssClass', 'specialButton')
                    self.addWidget(button, i, 3, 1, 1)
                    break

                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(checked):
            func(checked, *args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, checked, button):
        print(checked)
        self.display.insert(button.text())
