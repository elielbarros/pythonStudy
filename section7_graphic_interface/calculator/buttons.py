import math
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout

if TYPE_CHECKING:
    from info import Info
    from display import Display
    from main_window import MainWindow
from utils import isNumOrDot, isValidNumber
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
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Your Calculation'
        self._left = None
        self._right = None
        self._op = None

        self._equation = self._equationInitialValue

        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                if buttonText == '0':
                    button = Button(buttonText)
                    if not isNumOrDot(buttonText):
                        button.setProperty('cssClass', 'specialButton')
                        self._configSpecialButton(button)
                    self.addWidget(button, i, j, 1, 2)
                    buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button, )
                    self._connectButtonClicked(button, buttonSlot)

                    j += 1
                    nextButtonText = row[j]
                    button = Button(nextButtonText)
                    if not isNumOrDot(nextButtonText):
                        button.setProperty('cssClass', 'specialButton')
                        self._configSpecialButton(button)
                    self.addWidget(button, i, 2, 1, 1)
                    buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button, )
                    self._connectButtonClicked(button, buttonSlot)

                    j += 1
                    nextButtonText = row[j]
                    button = Button(nextButtonText)
                    if not isNumOrDot(nextButtonText):
                        button.setProperty('cssClass', 'specialButton')
                        self._configSpecialButton(button)
                    self.addWidget(button, i, 3, 1, 1)
                    buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button, )
                    self._connectButtonClicked(button, buttonSlot)

                    break

                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button, )
                self._connectButtonClicked(button, buttonSlot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                    button,
                    self._makeSlot(
                            self._operatorClicked,
                            button
                    )
            )

        if text == '=':
            self._connectButtonClicked(
                    button,
                    self._equal
            )

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        newDisplayValue = displayText + buttonText

        # print(newDisplayValue)

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button.text())

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/*^
        displayText = self.display.text()  # left number
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('You need type something.')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText

        self.equation = f'{self._left} {self._op} ??'

    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'

        try:
            result = 0.0

            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)

            self.display.clear()
            self.info.setText(f'{self.equation} = {result}')
            self._left = result
        except ZeroDivisionError:
            print('Zero Division Error')
        except OverflowError:
            print('Number is too big')
            self.info.setText(f'{self.equation} = error')
            self._left = None
            self.display.clear()
        finally:
            self._right = None

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
