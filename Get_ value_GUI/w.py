# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HB_Form(object):
    def setupUi(self, HB_Form):
        HB_Form.setObjectName("HB_Form")
        HB_Form.resize(970, 455)
        self.pushButton_start = QtWidgets.QPushButton(HB_Form)
        self.pushButton_start.setGeometry(QtCore.QRect(780, 90, 151, 71))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(HB_Form)
        self.pushButton_stop.setGeometry(QtCore.QRect(780, 180, 151, 71))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.formLayoutWidget_2 = QtWidgets.QWidget(HB_Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(690, 30, 241, 53))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.serial_portLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.serial_portLineEdit.setObjectName("serial_portLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.serial_portLineEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.progressBar = QtWidgets.QProgressBar(HB_Form)
        self.progressBar.setGeometry(QtCore.QRect(730, 390, 241, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_14 = QtWidgets.QLabel(HB_Form)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_save = QtWidgets.QPushButton(HB_Form)
        self.pushButton_save.setGeometry(QtCore.QRect(780, 270, 151, 71))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label = QtWidgets.QLabel(HB_Form)
        self.label.setGeometry(QtCore.QRect(730, 360, 81, 16))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(HB_Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 661, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(HB_Form)
        QtCore.QMetaObject.connectSlotsByName(HB_Form)

    def retranslateUi(self, HB_Form):
        _translate = QtCore.QCoreApplication.translate
        HB_Form.setWindowTitle(_translate("HB_Form", "Serial_Form"))
        self.pushButton_start.setText(_translate("HB_Form", "Start"))
        self.pushButton_stop.setText(_translate("HB_Form", "Stop"))
        self.label_2.setText(_translate("HB_Form", "Port"))
        self.label_3.setText(_translate("HB_Form", "Data Length"))
        self.label_14.setText(_translate("HB_Form", "Signal"))
        self.pushButton_save.setText(_translate("HB_Form", "Save"))
        self.label.setText(_translate("HB_Form", "DataLoading"))
