# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiDialogSalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSalir(object):
    def setupUi(self, DialogSalir):
        DialogSalir.setObjectName("DialogSalir")
        DialogSalir.resize(244, 237)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSalir)
        self.buttonBox.setGeometry(QtCore.QRect(40, 180, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DialogSalir)
        self.label.setGeometry(QtCore.QRect(60, 30, 119, 104))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/iconos/recursos/alert-icon-1563.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogSalir)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DialogSalir)
        self.buttonBox.accepted.connect(DialogSalir.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogSalir.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogSalir)

    def retranslateUi(self, DialogSalir):
        _translate = QtCore.QCoreApplication.translate
        DialogSalir.setWindowTitle(_translate("DialogSalir", "Salir"))
        self.label_2.setText(_translate("DialogSalir", "¿Desea salir?"))
import iconos_rc
