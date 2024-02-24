from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from typing import cast
from ui_window import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button_send.clicked.connect(self._changeLabelResult)

        self.line_name.installEventFilter(self)

    def _changeLabelResult(self):
        self.label_result.setText(self.line_name.text())

    def eventFilter(self, watched: QObject, event: QEvent):

        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            print(event.text())
            self.label_result.setText(self.line_name.text() + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
