import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from buttons import Button, ButtonsGrid
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
    window.addToVLayout(display)

    # Create Grid
    buttonsGrid = ButtonsGrid()
    window.verticalLayout.addLayout(buttonsGrid)

    # Create button 0
    button0 = Button('0')
    buttonsGrid.addWidget(button0, 0, 0)

    # Create button 1
    button1 = Button('1')
    buttonsGrid.addWidget(button1, 0, 1)

    # Create button 2
    button2 = Button('2')
    buttonsGrid.addWidget(button2, 0, 2)

    window.adjustFixedSize()
    window.show()
    app.exec()
