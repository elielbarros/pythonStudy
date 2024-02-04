"""
# English
QApplication is a fundamental class in the Qt framework for developing graphical user interfaces (GUI) in Python
using the PySide6 library. This class is responsible for managing the global resources and configurations required
for a Qt GUI application.

1. Application Initialization
2. Global Settings
3. Event Handling
4. Communication between Components
5. Resource Management
6. Application Termination

# Portuguese
- QApplication -

QApplication é uma classe fundamental no framework Qt para o desenvolvimento de interfaces gráficas de usuário (GUI)
em Python usando a biblioteca PySide6. Essa classe é responsável por gerenciar os recursos e configurações globais
necessários para uma aplicação GUI Qt.

1. Inicialização da Aplicação
2. Configurações Globais
3. Tratamento de Eventos
4. Comunicação entre Componentes
5. Gerenciamento de Recursos
6. Encerramento da Aplicação
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px;')
button.show()

app.exec()


