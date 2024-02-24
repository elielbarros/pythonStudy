from PySide6.QtWidgets import QMainWindow, QApplication
from ui_window import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button_send.clicked.connect(self._changeLabelResult)

    def _changeLabelResult(self):
        self.label_result.setText(self.line_name.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
