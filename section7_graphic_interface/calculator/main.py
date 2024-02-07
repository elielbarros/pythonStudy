import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel

from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    label1 = QLabel('Hello World')
    label1.setStyleSheet('font-size: 50px;')
    window.add_widget_to_vlayout(label1)

    window.adjust_fixed_size()
    window.show()
    app.exec()
