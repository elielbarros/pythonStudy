"""
QMainWindow and centralWidget
-> QApplicationn
    -> QMainWindow
        -> CentralWidget
            -> Layout
                -> Widget 1
                -> Widget 2
                -> Widget 3
    -> show
-> exec
"""

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Button
        self.button = self.make_button('Button0')
        self.button.clicked.connect(self.second_action_marked)

        self.button1 = self.make_button('Button1')

        self.button2 = self.make_button('Button2')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # Setting Window Title
        self.setWindowTitle('First Step with PySide')

        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button1, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button2, 2, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Status Bar Message')

        # menuBar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Menu 1')
        self.first_action = self.first_menu.addAction('Action 1')
        self.first_action.triggered.connect(self.change_status_bar_message)

        self.second_action = self.first_menu.addAction('Action 2')
        self.second_action.setCheckable(True)
        self.second_action.hovered.connect(self.second_action_marked)

    @Slot()
    def change_status_bar_message(self):
        self.status_bar.showMessage('Slot was executed')

    @Slot()
    def second_action_marked(self):
        print(f'Is checked? {self.second_action.isChecked()}')

    def make_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet('font-size: 20px;')
        return button


window = MyWindow()

window.show()

app.exec()
