# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 394)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.save = QHBoxLayout()
        self.save.setObjectName(u"save")

        self.verticalLayout_3.addLayout(self.save)

        self.YslugiTab = QTabWidget(Form)
        self.YslugiTab.setObjectName(u"YslugiTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.YslugiTab.sizePolicy().hasHeightForWidth())
        self.YslugiTab.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.numberdoc = QHBoxLayout()
        self.numberdoc.setObjectName(u"numberdoc")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.numberdoc.addWidget(self.label)

        self.input_doc_num = QLineEdit(self.tab)
        self.input_doc_num.setObjectName(u"input_doc_num")

        self.numberdoc.addWidget(self.input_doc_num)


        self.verticalLayout.addLayout(self.numberdoc)

        self.lastname = QHBoxLayout()
        self.lastname.setObjectName(u"lastname")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(110, 0))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.lastname.addWidget(self.label_2)

        self.input_client_lastname = QLineEdit(self.tab)
        self.input_client_lastname.setObjectName(u"input_client_lastname")

        self.lastname.addWidget(self.input_client_lastname)


        self.verticalLayout.addLayout(self.lastname)

        self.name = QHBoxLayout()
        self.name.setObjectName(u"name")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(110, 0))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.name.addWidget(self.label_3)

        self.input_client_name = QLineEdit(self.tab)
        self.input_client_name.setObjectName(u"input_client_name")

        self.name.addWidget(self.input_client_name)


        self.verticalLayout.addLayout(self.name)

        self.middlename = QHBoxLayout()
        self.middlename.setObjectName(u"middlename")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.middlename.addWidget(self.label_4)

        self.input_client_middname = QLineEdit(self.tab)
        self.input_client_middname.setObjectName(u"input_client_middname")

        self.middlename.addWidget(self.input_client_middname)


        self.verticalLayout.addLayout(self.middlename)

        self.address = QHBoxLayout()
        self.address.setObjectName(u"address")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(110, 0))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.address.addWidget(self.label_5)

        self.input_address = QLineEdit(self.tab)
        self.input_address.setObjectName(u"input_address")

        self.address.addWidget(self.input_address)


        self.verticalLayout.addLayout(self.address)

        self.tel = QHBoxLayout()
        self.tel.setObjectName(u"tel")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(110, 0))
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.tel.addWidget(self.label_6)

        self.input_tel = QLineEdit(self.tab)
        self.input_tel.setObjectName(u"input_tel")

        self.tel.addWidget(self.input_tel)


        self.verticalLayout.addLayout(self.tel)

        self.YslugiTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yslugi = QLabel(self.tab_2)
        self.yslugi.setObjectName(u"yslugi")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.yslugi.sizePolicy().hasHeightForWidth())
        self.yslugi.setSizePolicy(sizePolicy2)
        self.yslugi.setMinimumSize(QSize(110, 0))
        self.yslugi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.yslugi.setMargin(0)

        self.horizontalLayout_2.addWidget(self.yslugi)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.tab_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setIconSize(QSize(16, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.tab_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.tab_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.tab_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_6 = QCheckBox(self.tab_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_5 = QCheckBox(self.tab_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_2.addWidget(self.checkBox_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.YslugiTab.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.YslugiTab)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_savefolder = QPushButton(Form)
        self.button_savefolder.setObjectName(u"button_savefolder")

        self.horizontalLayout.addWidget(self.button_savefolder)

        self.showsavepath = QLineEdit(Form)
        self.showsavepath.setObjectName(u"showsavepath")

        self.horizontalLayout.addWidget(self.showsavepath)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.create_doc_event = QPushButton(Form)
        self.create_doc_event.setObjectName(u"create_doc_event")

        self.verticalLayout_3.addWidget(self.create_doc_event)


        self.retranslateUi(Form)

        self.YslugiTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430: ", None))
        self.input_doc_num.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f: ", None))
        self.input_client_lastname.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f: ", None))
        self.input_client_name.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e: ", None))
        self.input_client_middname.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441: ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d: ", None))
        self.input_tel.setPlaceholderText("")
        self.YslugiTab.setTabText(self.YslugiTab.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.yslugi.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u043b\u0443\u0433\u0438:", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u043e\u0439 \u0431\u0430\u0437\u044b \u0438 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0430\u0432\u043e\u0432\u043e\u0439 \u043f\u043e\u0437\u0438\u0446\u0438\u0438", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 ", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"2", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"4", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.YslugiTab.setTabText(self.YslugiTab.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.button_savefolder.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u043f\u0430\u043f\u043a\u0443:", None))
        self.create_doc_event.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

