from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

from utils import isEmpty
from variables import BIGGEST_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIGGEST_FONT_SIZE}px;')
        self.setMinimumHeight(BIGGEST_FONT_SIZE * 1.1)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key == KEYS.Key_Escape

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete or text == 'd':
            self.delPressed.emit()
            return event.ignore()

        if isEsc or text == 'c':
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        print(f'text: {text}')

        # return super().keyPressEvent(event)  # Will remove possibility to type with keyboard


