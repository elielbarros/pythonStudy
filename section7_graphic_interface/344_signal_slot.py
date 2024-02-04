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
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
# Setting Window Title
window.setWindowTitle('First Step with PySide')

button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px;')

button1 = QPushButton('Button1')
button1.setStyleSheet('font-size: 20px;')

button2 = QPushButton('Button2')
button2.setStyleSheet('font-size: 20px;')

layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button1, 1, 2, 1, 1)
layout.addWidget(button2, 2, 1, 1, 2)

# statusBar
# Show message using status bar
status_bar = window.statusBar()
status_bar.showMessage('Status Bar Message')


@Slot()
def slot_example(status_bar_parameter):
    def inner_function():
        status_bar_parameter.showMessage('Slot was executed')

    return inner_function


# menuBar
# creating menu using window.menuBar()
menu = window.menuBar()

# Add first option to menu
first_menu = menu.addMenu('Menu 1')

# Add first action option for first menu option
first_action = first_menu.addAction('Action 1')

# When user click on Action 1, first_action will trigger the method slot_example() and print 123
first_action.triggered.connect(slot_example(status_bar))

# Creating a 'check-able' action
second_action = first_menu.addAction('Action 2')
second_action.setCheckable(True)


@Slot()
def another_slot(checked):
    print(f'Is checked? {checked}')


@Slot()
def slot_three(action):
    def inner_function():
        another_slot(action.isChecked())

    return inner_function


# second_action.toggled.connect(another_slot)
second_action.hovered.connect(slot_three(second_action))

button.clicked.connect(slot_three(second_action))

# Using WINDOW to show central widget
window.show()

app.exec()
