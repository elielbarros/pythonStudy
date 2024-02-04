"""
# English
PySide6

Library that enables the development of graphical user interfaces (GUI) in Python using the Qt 6 framework. Qt is a
widely used software development framework for creating applications with elegant, cross-platform graphical user
interfaces. PySide6 is one of the Python implementations of the Qt API, and it allows developers to create
interactive desktop applications.

How install
    - pip install pyside6

Documentation
    - https://doc.qt.io/qtforpython-6/quickstart.html

# Portuguese
PySide6

Biblioteca que permite o desenvolvimento de interfaces gráficas de usuário (GUI) em Python usando o framework Qt 6.
Qt é uma estrutura de desenvolvimento de software amplamente utilizada para criar aplicativos com interfaces gráficas
de usuário elegantes e multiplataforma. PySide6 é uma das implementações Python da API Qt, e ela permite que
desenvolvedores criem aplicações desktop interativas.

Como instalar?
    - pip install pyside6

Documetacao
    - https://doc.qt.io/qtforpython-6/quickstart.html

"""
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)
