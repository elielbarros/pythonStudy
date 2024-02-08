import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from display import Display
from main_window import MainWindow
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':

    # Create application
    app = QApplication(sys.argv)

    # Setup Theme
    setupTheme()

    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Create display
    display = Display()
    window.addWidgetToVLayout(display)

    window.adjustFixedSize()
    window.show()
    app.exec()
