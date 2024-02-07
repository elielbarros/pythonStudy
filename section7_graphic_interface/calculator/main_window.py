from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configure Basic Layout
        self.centralWidget = QWidget()
        self.verticalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.centralWidget)

        # Configure Window Title
        self.setWindowTitle('CALCULATOR')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.verticalLayout.addWidget(widget)