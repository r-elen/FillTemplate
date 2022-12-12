
from PySide6 import QtWidgets
from ui.form.MainForm import Ui_Form


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self) -> None:
        """
        Донастройка Ui
        :return: None
        """
        self.setWindowTitle("DocCreator")
        self.ui.client_lastname.setPlaceholderText("Иванов")

        # self.ui.but_savingdoc

    def initChild(self) -> None:
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
        # self.pb_1.clicked.connect(self.print_hello)
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
