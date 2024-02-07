from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configure Basic Layout
        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)

        # Configure Window Title
        self.setWindowTitle('CALCULATOR')

    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
