import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from buttons import ButtonsGrid
from display import Display
from main_window import MainWindow
from styles import setupTheme
from variables import WINDOW_ICON_PATH
from info import Info

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

    # Create Info
    info = Info('')
    window.addToVLayout(info)

    # Create display
    display = Display()
    window.addToVLayout(display)

    # Create Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.verticalLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
