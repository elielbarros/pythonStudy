import sys
import time

from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        for i in range(5):
            print(i)
            time.sleep(1)
        self.label1.setText('1 ended')

    def hardWork2(self):
        for i in range(5):
            print(i)
            time.sleep(1)
        self.label2.setText('2 ended')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
