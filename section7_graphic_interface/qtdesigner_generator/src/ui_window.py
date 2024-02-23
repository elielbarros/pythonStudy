# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        font = QFont()
        font.setPointSize(40)
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_result, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        font1 = QFont()
        font1.setPointSize(30)
        self.label_name.setFont(font1)

        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)

        self.line_name = QLineEdit(self.centralwidget)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setFont(font1)

        self.gridLayout_2.addWidget(self.line_name, 0, 1, 1, 1)

        self.button_send = QPushButton(self.centralwidget)
        self.button_send.setObjectName(u"button_send")
        self.button_send.setFont(font1)

        self.gridLayout_2.addWidget(self.button_send, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"Hello world!", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Seu nome:", None))
        self.line_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digit your name", None))
        self.button_send.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

