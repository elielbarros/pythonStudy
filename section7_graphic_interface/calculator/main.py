import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel

from display import Display
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':

    # Create application
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Create display
    display = Display()
    window.addWidgetToVLayout(display)

    label1 = QLabel('Hello World')
    label1.setStyleSheet('font-size: 50px;')
    window.addWidgetToVLayout(label1)

    window.adjustFixedSize()
    window.show()
    app.exec()
