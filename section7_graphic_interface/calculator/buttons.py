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
            ['N', '0', '.', '=']
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Calculation result'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue

        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _number(self, *args):
        print(f'text: {args}')

    def _makeGrid(self):
        self.display.eqPressed.connect(self._equal)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertButtonTextToDisplay)
        self.display.operatorPressed.connect(self._operatorClicked)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button.text(), )
                self._connectButtonClicked(button, buttonSlot)

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == '◀':
            self._connectButtonClicked(button, self._backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonClicked(
                    button,
                    self._makeSlot(
                            self._operatorClicked,
                            text
                    )
            )

        if text == '=':
            self._connectButtonClicked(
                    button,
                    self._equal
            )

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return

        number = self._convertToNumber(displayText) * -1

        self.display.setText(str(number))

    def _convertToNumber(self, displayText):
        number = float(displayText)

        if number.is_integer():
            number = int(number)

        return number

    @Slot()
    def _insertButtonTextToDisplay(self, text):
        buttonText = text
        displayText = self.display.text()
        newDisplayValue = displayText + buttonText

        # print(newDisplayValue)

        if not isValidNumber(newDisplayValue):
            self.display.setFocus()
            return

        self.display.insert(buttonText)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _operatorClicked(self, buttonText):
        displayText = self.display.text()  # left number
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('You need type something.')
            self.display.setFocus()
            return

        if self._left is None:
            self._left = self._convertToNumber(displayText)

        self._op = buttonText

        self.equation = f'{self._left} {self._op} ??'
        self.display.setFocus()

    @Slot()
    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('You need type something.')
            return

        self._right = self._convertToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'

        try:
            result = 0.0
            isintOrFloat = isinstance(self._left, float) | isinstance(self._left, int)
            if '^' in self.equation and isintOrFloat:
                result = self._convertToNumber(math.pow(self._left, self._right))
            else:
                result = eval(self.equation)

            self.display.clear()
            self.info.setText(f'{self.equation} = {result}')
            self._left = result
        except ZeroDivisionError:
            self._showError('You are trying to divide number by zero')
        except OverflowError:
            self._showError('This calculation cannot be performed')
            self.info.setText(f'{self.equation} = error')
            self._left = None
            self.display.clear()
        finally:
            self._right = None
            self.display.setFocus()

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()

        # msgBox = self.window.makeMsgBox()
        # msgBox.setText(text)
        # msgBox.setInformativeText('Lorem ipsum dolor sit amet')
        # msgBox.setIcon(msgBox.Icon.Critical)

        # msgBox.setStandardButtons(
        #         msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel
        # )

        # msgBox.button(msgBox.StandardButton.Ok).setText('Agreed')

        # result = msgBox.exec()

        # if result == msgBox.StandardButton.Ok:
        #     print('User clicked on the button "Ok"')
        # if result == msgBox.StandardButton.Cancel:
        #     print('User clicked on the button "Cancel"')

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox
