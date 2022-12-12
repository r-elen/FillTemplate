
from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initChilds()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Донастройка Ui
        :return: None
        """
        self.pb_1 = QtWidgets.QPushButton("Кнопка", self)

    def initChilds(self) -> None:
        """
        Инициализация дочерних окон
        :return: None
        """
        # self.win_2 = ChildWindow() #импорт окна
        pass

    def initSignals(self) -> None:
        """
        Инициализация сигнала
        :return: None
        """
        self.pb_1.clicked.connect(self.print_hello)

    def print_hello(self):
        print('Hello!')


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
