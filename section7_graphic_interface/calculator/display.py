from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

from variables import BIGGEST_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
    eqRequested = Signal()

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
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]

        if isEnter:
            self.eqRequested.emit()
            return event.ignore()

        # return super().keyPressEvent(event)  # Will remove possibility to type with keyboard


