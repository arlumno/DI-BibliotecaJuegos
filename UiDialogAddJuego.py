# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiDialogAddJuego.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddJuego(object):
    def setupUi(self, DialogAddJuego):
        DialogAddJuego.setObjectName("DialogAddJuego")
        DialogAddJuego.resize(522, 554)
        self.label_17 = QtWidgets.QLabel(DialogAddJuego)
        self.label_17.setGeometry(QtCore.QRect(30, 250, 91, 29))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.teObservaciones = QtWidgets.QPlainTextEdit(DialogAddJuego)
        self.teObservaciones.setGeometry(QtCore.QRect(30, 420, 461, 81))
        self.teObservaciones.setObjectName("teObservaciones")
        self.label_18 = QtWidgets.QLabel(DialogAddJuego)
        self.label_18.setGeometry(QtCore.QRect(30, 390, 91, 29))
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.teDescripcion = QtWidgets.QPlainTextEdit(DialogAddJuego)
        self.teDescripcion.setGeometry(QtCore.QRect(30, 280, 461, 101))
        self.teDescripcion.setObjectName("teDescripcion")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(DialogAddJuego)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 210, 461, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.cbGenero = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.cbGenero.setObjectName("cbGenero")
        self.horizontalLayout_3.addWidget(self.cbGenero)
        self.etGenero = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.etGenero.setObjectName("etGenero")
        self.horizontalLayout_3.addWidget(self.etGenero)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(DialogAddJuego)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 160, 461, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.cbDificultad = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbDificultad.setObjectName("cbDificultad")
        self.horizontalLayout_2.addWidget(self.cbDificultad)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.cbPropietario = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbPropietario.setObjectName("cbPropietario")
        self.horizontalLayout_2.addWidget(self.cbPropietario)
        self.bAddPropietario = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bAddPropietario.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAddPropietario.setIcon(icon)
        self.bAddPropietario.setObjectName("bAddPropietario")
        self.horizontalLayout_2.addWidget(self.bAddPropietario)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(DialogAddJuego)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 59, 461, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.etNombre = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.etNombre.setObjectName("etNombre")
        self.horizontalLayout_4.addWidget(self.etNombre)
        self.horizontalLayoutWidget = QtWidgets.QWidget(DialogAddJuego)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 110, 461, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.sbMinJugadores = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sbMinJugadores.setFont(font)
        self.sbMinJugadores.setProperty("value", 1)
        self.sbMinJugadores.setObjectName("sbMinJugadores")
        self.horizontalLayout.addWidget(self.sbMinJugadores)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.sbMaxJugadores = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sbMaxJugadores.setFont(font)
        self.sbMaxJugadores.setProperty("value", 1)
        self.sbMaxJugadores.setObjectName("sbMaxJugadores")
        self.horizontalLayout.addWidget(self.sbMaxJugadores)
        self.label_8 = QtWidgets.QLabel(DialogAddJuego)
        self.label_8.setGeometry(QtCore.QRect(3, 13, 511, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.bCerrar = QtWidgets.QPushButton(DialogAddJuego)
        self.bCerrar.setGeometry(QtCore.QRect(400, 512, 91, 31))
        self.bCerrar.setObjectName("bCerrar")
        self.bGuardar = QtWidgets.QPushButton(DialogAddJuego)
        self.bGuardar.setGeometry(QtCore.QRect(30, 510, 91, 31))
        self.bGuardar.setObjectName("bGuardar")

        self.retranslateUi(DialogAddJuego)
        QtCore.QMetaObject.connectSlotsByName(DialogAddJuego)

    def retranslateUi(self, DialogAddJuego):
        _translate = QtCore.QCoreApplication.translate
        DialogAddJuego.setWindowTitle(_translate("DialogAddJuego", "Dialog"))
        self.label_17.setText(_translate("DialogAddJuego", "Descripción"))
        self.label_18.setText(_translate("DialogAddJuego", "Observaciones"))
        self.label_16.setText(_translate("DialogAddJuego", "Genero:"))
        self.label_19.setText(_translate("DialogAddJuego", "Dificultad"))
        self.label_13.setText(_translate("DialogAddJuego", "Propietario:"))
        self.label_11.setText(_translate("DialogAddJuego", "Nombre:"))
        self.label_12.setText(_translate("DialogAddJuego", "Jugadores:"))
        self.label_14.setText(_translate("DialogAddJuego", "Mínimo"))
        self.label_15.setText(_translate("DialogAddJuego", "Máximo"))
        self.label_8.setText(_translate("DialogAddJuego", "Añadir Nuevo Juego"))
        self.bCerrar.setText(_translate("DialogAddJuego", "Cerrar"))
        self.bGuardar.setText(_translate("DialogAddJuego", "Guardar"))
import iconos_rc
