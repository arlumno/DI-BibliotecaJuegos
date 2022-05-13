# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiDialogJuego.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogJuego(object):
    def setupUi(self, DialogJuego):
        DialogJuego.setObjectName("DialogJuego")
        DialogJuego.resize(510, 556)
        DialogJuego.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(178, 236, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 3px;\n"
"    border: 1px solid gray;\n"
"\n"
"}\n"
"QComboBox{\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    min-width: 6em;\n"
"}\n"
"")
        self.label_17 = QtWidgets.QLabel(DialogJuego)
        self.label_17.setGeometry(QtCore.QRect(30, 190, 91, 29))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.teObservaciones = QtWidgets.QPlainTextEdit(DialogJuego)
        self.teObservaciones.setGeometry(QtCore.QRect(30, 360, 461, 121))
        self.teObservaciones.setReadOnly(True)
        self.teObservaciones.setObjectName("teObservaciones")
        self.label_18 = QtWidgets.QLabel(DialogJuego)
        self.label_18.setGeometry(QtCore.QRect(30, 330, 91, 29))
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.teDescripcion = QtWidgets.QPlainTextEdit(DialogJuego)
        self.teDescripcion.setGeometry(QtCore.QRect(30, 220, 461, 101))
        self.teDescripcion.setReadOnly(True)
        self.teDescripcion.setObjectName("teDescripcion")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(DialogJuego)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 100, 451, 30))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.lbGenero = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbGenero.setFont(font)
        self.lbGenero.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbGenero.setObjectName("lbGenero")
        self.horizontalLayout_3.addWidget(self.lbGenero)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_3.addWidget(self.label_20)
        self.lbDificultad = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbDificultad.setFont(font)
        self.lbDificultad.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbDificultad.setObjectName("lbDificultad")
        self.horizontalLayout_3.addWidget(self.lbDificultad)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(DialogJuego)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 140, 451, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.lbPropietario = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbPropietario.setFont(font)
        self.lbPropietario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbPropietario.setObjectName("lbPropietario")
        self.horizontalLayout_2.addWidget(self.lbPropietario)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.lbAlta = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbAlta.setFont(font)
        self.lbAlta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbAlta.setObjectName("lbAlta")
        self.horizontalLayout_2.addWidget(self.lbAlta)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.lbPropietario_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbPropietario_3.setFont(font)
        self.lbPropietario_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbPropietario_3.setObjectName("lbPropietario_3")
        self.horizontalLayout_2.addWidget(self.lbPropietario_3)
        self.lbCod = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbCod.setFont(font)
        self.lbCod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbCod.setObjectName("lbCod")
        self.horizontalLayout_2.addWidget(self.lbCod)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(DialogJuego)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 59, 451, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lbNombre = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbNombre.setFont(font)
        self.lbNombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbNombre.setObjectName("lbNombre")
        self.horizontalLayout_4.addWidget(self.lbNombre)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.lbNJugadores = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbNJugadores.setFont(font)
        self.lbNJugadores.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbNJugadores.setObjectName("lbNJugadores")
        self.horizontalLayout_4.addWidget(self.lbNJugadores)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_8 = QtWidgets.QLabel(DialogJuego)
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
        self.bCerrar = QtWidgets.QPushButton(DialogJuego)
        self.bCerrar.setGeometry(QtCore.QRect(400, 512, 91, 31))
        self.bCerrar.setObjectName("bCerrar")
        self.bEliminar = QtWidgets.QPushButton(DialogJuego)
        self.bEliminar.setGeometry(QtCore.QRect(30, 510, 91, 31))
        self.bEliminar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 100,100, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEliminar.setIcon(icon)
        self.bEliminar.setIconSize(QtCore.QSize(24, 24))
        self.bEliminar.setObjectName("bEliminar")
        self.bEditar = QtWidgets.QPushButton(DialogJuego)
        self.bEditar.setGeometry(QtCore.QRect(140, 510, 91, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/recursos/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEditar.setIcon(icon1)
        self.bEditar.setIconSize(QtCore.QSize(20, 20))
        self.bEditar.setObjectName("bEditar")

        self.retranslateUi(DialogJuego)
        QtCore.QMetaObject.connectSlotsByName(DialogJuego)

    def retranslateUi(self, DialogJuego):
        _translate = QtCore.QCoreApplication.translate
        DialogJuego.setWindowTitle(_translate("DialogJuego", "Información Juego"))
        self.label_17.setText(_translate("DialogJuego", "Descripción"))
        self.teObservaciones.setPlainText(_translate("DialogJuego", "---"))
        self.label_18.setText(_translate("DialogJuego", "Observaciones"))
        self.teDescripcion.setPlainText(_translate("DialogJuego", "---"))
        self.label_16.setText(_translate("DialogJuego", "Genero:"))
        self.lbGenero.setText(_translate("DialogJuego", "---"))
        self.label_20.setText(_translate("DialogJuego", "Dificultad"))
        self.lbDificultad.setText(_translate("DialogJuego", "---"))
        self.label_14.setText(_translate("DialogJuego", "Propietario:"))
        self.lbPropietario.setText(_translate("DialogJuego", "---"))
        self.label_15.setText(_translate("DialogJuego", "Alta: "))
        self.lbAlta.setText(_translate("DialogJuego", "---"))
        self.lbPropietario_3.setText(_translate("DialogJuego", "Cod:"))
        self.lbCod.setText(_translate("DialogJuego", "---"))
        self.label_11.setText(_translate("DialogJuego", "Nombre:"))
        self.lbNombre.setText(_translate("DialogJuego", "---"))
        self.label_12.setText(_translate("DialogJuego", "Jugadores:"))
        self.lbNJugadores.setText(_translate("DialogJuego", "0"))
        self.label_8.setText(_translate("DialogJuego", "Juego"))
        self.bCerrar.setText(_translate("DialogJuego", "Cerrar"))
        self.bEliminar.setText(_translate("DialogJuego", "Eliminar"))
        self.bEditar.setText(_translate("DialogJuego", "Modificar"))
import iconos_rc