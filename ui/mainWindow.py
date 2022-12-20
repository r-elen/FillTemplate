
from PySide6 import QtWidgets, QtCore

from ui.form.MainForm import Ui_Form
import doc.replace2 as r


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()

        self.ui.setupUi(self)
        self.initUi()

        self.initSignals()

    def initUi(self) -> None:
        """
        Донастройка Ui
        :return: None
        """
        self.setWindowTitle("DocCreator")
        setting = QtCore.QSettings("DocCreator")

        # self.ui.button_savefolder.setPlainText(setting.value("saveFolder", ""))
        self.ui.input_client_middname.setText("")

        # self.ui.but_savingdoc

    # def initChild(self) -> None:
    #     """
    #     Инициализация дочерних окон
    #     :return: None
    #     """
    #     # self.win_2 = ChildWindow() #импорт окна
    #     pass

    def initSignals(self) -> None:
        """
        Инициализация сигнала
        :return: None
        """
        self.ui.button_savefolder.clicked.connect(self.chooseFolderButton)
        self.ui.create_doc_event.clicked.connect(self.createDocButton)

    def input_info(self):
        doc_num = r.create_num(self.ui.input_doc_num.text())  # получение данных из строки ввода пользователем
        client_lastname = self.ui.input_client_lastname.text()
        client_name = self.ui.input_client_name.text()
        client_middname = self.ui.input_client_middname.text()
        address = self.ui.input_address.text()
        tel = self.ui.input_tel.text()
        date_1 = r.create_date()
        client_full_name = r.create_full_name(client_lastname, client_name, client_middname)
        initials = r.create_initials(client_lastname, client_name, client_middname)

        list_info = [doc_num, date_1, client_full_name, address, initials, tel]

        return list_info

    def chooseFolderButton(self):
        pass

    def createDocButton(self):
        list_temps = r.create_template_list()
        list_info = self.input_info()
        tmp_doc = "Шаблон 1.docx"
        name_save_doc = ' '.join(['Договор', list_info[0]])

        r.repl_template(tmp_doc, name_save_doc, list_temps, list_info)
        QtWidgets.QMessageBox.about(self, "Уведомление", "Обработка выполнена")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
