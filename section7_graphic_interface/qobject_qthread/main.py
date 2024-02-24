import sys
import time

from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progress = Signal(str)
    finished = Signal(str)

    def run(self):
        self.started.emit('0 %')
        for i in range(5):
            percentage = i * 100 / 5
            self.progress.emit(f'{str(percentage)} %')
            time.sleep(1)
        self.finished.emit('100 %')


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread: QObject = self._thread

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Conectar o Run
        thread.started.connect(worker.run)

        # Quando a thread terminar a execucao, finalizar o trabalho
        worker.finished.connect(thread.quit)

        # Para que a Thread e o Worker sejam removidos da memoria
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(thread.deleteLater)

        # Apos configurar worker e thread
        # Configurar as acoes para cada estado do worker
        worker.started.connect(self._worker1Started)
        worker.progress.connect(self._worker1Progress)
        worker.finished.connect(self._worker1Finished)

        thread.start()

    def _worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker 1 started')

    def _worker1Progress(self, value):
        self.label1.setText(value)
        print('worker 1 in progress')

    def _worker1Finished(self, value):
        self.label1.setText(value)
        self.button1.setDisabled(False)
        print('worker 1 has finished')


    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread: QObject = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Conectar o Run
        thread.started.connect(worker.run)

        # Quando a thread terminar a execucao, finalizar o trabalho
        worker.finished.connect(thread.quit)

        # Para que a Thread e o Worker sejam removidos da memoria
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(thread.deleteLater)

        # Apos configurar worker e thread
        # Configurar as acoes para cada estado do worker
        worker.started.connect(self._worker2Started)
        worker.progress.connect(self._worker2Progress)
        worker.finished.connect(self._worker2Finished)

        thread.start()

    def _worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 started')

    def _worker2Progress(self, value):
        self.label2.setText(value)
        print('worker 2 in progress')

    def _worker2Finished(self, value):
        self.label2.setText(value)
        self.button2.setDisabled(False)
        print('worker 2 has finished')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
