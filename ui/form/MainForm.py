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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(459, 428)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numberdoc = QHBoxLayout()
        self.numberdoc.setObjectName(u"numberdoc")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.numberdoc.addWidget(self.label)

        self.input_doc_num = QLineEdit(self.groupBox)
        self.input_doc_num.setObjectName(u"input_doc_num")

        self.numberdoc.addWidget(self.input_doc_num)


        self.verticalLayout_2.addLayout(self.numberdoc)

        self.lastname = QHBoxLayout()
        self.lastname.setObjectName(u"lastname")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(110, 0))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.lastname.addWidget(self.label_2)

        self.input_client_lastname = QLineEdit(self.groupBox)
        self.input_client_lastname.setObjectName(u"input_client_lastname")

        self.lastname.addWidget(self.input_client_lastname)


        self.verticalLayout_2.addLayout(self.lastname)

        self.name = QHBoxLayout()
        self.name.setObjectName(u"name")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(110, 0))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.name.addWidget(self.label_3)

        self.input_client_name = QLineEdit(self.groupBox)
        self.input_client_name.setObjectName(u"input_client_name")

        self.name.addWidget(self.input_client_name)


        self.verticalLayout_2.addLayout(self.name)

        self.middlename = QHBoxLayout()
        self.middlename.setObjectName(u"middlename")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.middlename.addWidget(self.label_4)

        self.input_client_middname = QLineEdit(self.groupBox)
        self.input_client_middname.setObjectName(u"input_client_middname")

        self.middlename.addWidget(self.input_client_middname)


        self.verticalLayout_2.addLayout(self.middlename)

        self.address = QHBoxLayout()
        self.address.setObjectName(u"address")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(110, 0))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.address.addWidget(self.label_5)

        self.input_address = QLineEdit(self.groupBox)
        self.input_address.setObjectName(u"input_address")

        self.address.addWidget(self.input_address)


        self.verticalLayout_2.addLayout(self.address)

        self.tel = QHBoxLayout()
        self.tel.setObjectName(u"tel")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(110, 0))
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.tel.addWidget(self.label_6)

        self.input_tel = QLineEdit(self.groupBox)
        self.input_tel.setObjectName(u"input_tel")

        self.tel.addWidget(self.input_tel)


        self.verticalLayout_2.addLayout(self.tel)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(110, 0))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.comboBox_servises = QComboBox(self.groupBox_2)
        self.comboBox_servises.setObjectName(u"comboBox_servises")

        self.horizontalLayout_2.addWidget(self.comboBox_servises)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chooseFolderButton = QPushButton(Form)
        self.chooseFolderButton.setObjectName(u"chooseFolderButton")

        self.horizontalLayout.addWidget(self.chooseFolderButton)

        self.showsavepath = QLineEdit(Form)
        self.showsavepath.setObjectName(u"showsavepath")

        self.horizontalLayout.addWidget(self.showsavepath)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 15, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.createDocButton = QPushButton(Form)
        self.createDocButton.setObjectName(u"createDocButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.createDocButton.sizePolicy().hasHeightForWidth())
        self.createDocButton.setSizePolicy(sizePolicy3)
        self.createDocButton.setMaximumSize(QSize(16777215, 16777215))
        self.createDocButton.setBaseSize(QSize(0, 0))
        self.createDocButton.setTabletTracking(False)
        self.createDocButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.createDocButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435", None))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0443\u0441\u043b\u0443\u0433\u0438:", None))
        self.chooseFolderButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u043f\u0430\u043f\u043a\u0443:", None))
        self.createDocButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

