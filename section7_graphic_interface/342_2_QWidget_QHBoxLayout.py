import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout

app = QApplication(sys.argv)

button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px;')

button1 = QPushButton('Button1')
button1.setStyleSheet('font-size: 40px;')

# Generic Widget
# Receives a Layout
# Cannot add a Widget
central_widget = QWidget()

# To show QWidget it is necessary a Layout, that will be used to add Widgets
# QHBoxLayout is a HORIZONTAL layout
layout = QHBoxLayout()

# Set layout on central widget
central_widget.setLayout(layout)

# Adding buttons to layout
layout.addWidget(button)
layout.addWidget(button1)

# Showing central widget
central_widget.show()

app.exec()
