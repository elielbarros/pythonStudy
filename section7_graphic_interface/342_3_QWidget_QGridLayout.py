import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px;')

button1 = QPushButton('Button1')
button1.setStyleSheet('font-size: 20px;')

button2 = QPushButton('Button2')
button2.setStyleSheet('font-size: 20px;')

# Generic Widget
# Receives a Layout
# Cannot add a Widget
central_widget = QWidget()

# To show QWidget it is necessary a Layout, that will be used to add Widgets
# QGridLayout is a changeable layout
layout = QGridLayout()

# Set layout on central widget
central_widget.setLayout(layout)

# Adding buttons to layout in a HORIZONTAL WAY
# layout.addWidget(button, 1, 1)
# layout.addWidget(button1, 1, 2)

# Adding buttons to layout in a VERTICAL WAY
# layout.addWidget(button, 1, 1)
# layout.addWidget(button1, 2, 1)

# It is also possible to use a third button with two buttons in a horizontal WAY and the third button in a vertical WAY
layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button1, 1, 2, 1, 1)

# The third parameter means that in a row the button is not expandable
# The fourth parameter means that in columns the button is expandable covering any existence column
# BUTTON1 # BUTTON 2 #
#       BUTTON3      #
layout.addWidget(button2, 2, 1, 1, 2)

# Showing central widget
central_widget.show()

app.exec()
