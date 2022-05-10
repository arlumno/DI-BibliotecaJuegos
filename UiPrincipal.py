# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        MainWindow.setMinimumSize(QtCore.QSize(900, 675))
        MainWindow.setMaximumSize(QtCore.QSize(900, 675))
        MainWindow.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(178, 236, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 3px;\n"
"    border: 1px solid gray;\n"
"\n"
"}\n"
"QComboBox{\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        palette = QtGui.QPalette()
        self.centralwidget.setPalette(palette)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 881, 581))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.listado = QtWidgets.QWidget()
        self.listado.setAutoFillBackground(True)
        self.listado.setStyleSheet("")
        self.listado.setObjectName("listado")
        self.twListadoJuegos = QtWidgets.QTableWidget(self.listado)
        self.twListadoJuegos.setGeometry(QtCore.QRect(20, 120, 841, 411))
        self.twListadoJuegos.setMinimumSize(QtCore.QSize(841, 0))
        self.twListadoJuegos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twListadoJuegos.setObjectName("twListadoJuegos")
        self.twListadoJuegos.setColumnCount(8)
        self.twListadoJuegos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.twListadoJuegos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.twListadoJuegos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twListadoJuegos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twListadoJuegos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.twListadoJuegos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.twListadoJuegos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.twListadoJuegos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.twListadoJuegos.setHorizontalHeaderItem(7, item)
        self.twListadoJuegos.horizontalHeader().setSortIndicatorShown(False)
        self.label_2 = QtWidgets.QLabel(self.listado)
        self.label_2.setGeometry(QtCore.QRect(2, 10, 871, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.listado)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 841, 71))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 17, 671, 45))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.etNombre = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        self.etNombre.setPalette(palette)
        self.etNombre.setObjectName("etNombre")
        self.verticalLayout.addWidget(self.etNombre)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.cbGenero = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbGenero.setObjectName("cbGenero")
        self.verticalLayout_2.addWidget(self.cbGenero)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.cbDificultad = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbDificultad.setObjectName("cbDificultad")
        self.verticalLayout_3.addWidget(self.cbDificultad)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.cbMinJugadores = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbMinJugadores.setObjectName("cbMinJugadores")
        self.horizontalLayout.addWidget(self.cbMinJugadores)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.cbMaxJugadores = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbMaxJugadores.setObjectName("cbMaxJugadores")
        self.horizontalLayout.addWidget(self.cbMaxJugadores)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.cbPropietario = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbPropietario.setObjectName("cbPropietario")
        self.verticalLayout_4.addWidget(self.cbPropietario)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.bReiniciarFiltros = QtWidgets.QPushButton(self.groupBox)
        self.bReiniciarFiltros.setGeometry(QtCore.QRect(754, 17, 81, 46))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/recursos/eliminar_filtros.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bReiniciarFiltros.setIcon(icon)
        self.bReiniciarFiltros.setIconSize(QtCore.QSize(24, 24))
        self.bReiniciarFiltros.setObjectName("bReiniciarFiltros")
        self.bFiltrar = QtWidgets.QPushButton(self.groupBox)
        self.bFiltrar.setGeometry(QtCore.QRect(677, 17, 75, 46))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/recursos/filtrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bFiltrar.setIcon(icon1)
        self.bFiltrar.setIconSize(QtCore.QSize(24, 24))
        self.bFiltrar.setObjectName("bFiltrar")
        self.label_12 = QtWidgets.QLabel(self.listado)
        self.label_12.setGeometry(QtCore.QRect(31, 532, 151, 20))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.listado, "")
        self.add = QtWidgets.QWidget()
        self.add.setAutoFillBackground(True)
        self.add.setObjectName("add")
        self.label_8 = QtWidgets.QLabel(self.add)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 871, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.add)
        self.groupBox_2.setGeometry(QtCore.QRect(680, 70, 171, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.bImportarBD = QtWidgets.QPushButton(self.groupBox_2)
        self.bImportarBD.setGeometry(QtCore.QRect(10, 30, 149, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/recursos/Misc_Upload_Database_Icon_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bImportarBD.setIcon(icon2)
        self.bImportarBD.setIconSize(QtCore.QSize(32, 32))
        self.bImportarBD.setObjectName("bImportarBD")
        self.bExportarBD = QtWidgets.QPushButton(self.groupBox_2)
        self.bExportarBD.setGeometry(QtCore.QRect(10, 100, 149, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/recursos/Download Database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bExportarBD.setIcon(icon3)
        self.bExportarBD.setIconSize(QtCore.QSize(32, 32))
        self.bExportarBD.setObjectName("bExportarBD")
        self.bEliminarBD = QtWidgets.QPushButton(self.groupBox_2)
        self.bEliminarBD.setGeometry(QtCore.QRect(10, 210, 149, 51))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/recursos/Remove_from_database_Icon_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEliminarBD.setIcon(icon4)
        self.bEliminarBD.setIconSize(QtCore.QSize(32, 32))
        self.bEliminarBD.setObjectName("bEliminarBD")
        self.groupBox_3 = QtWidgets.QGroupBox(self.add)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 70, 151, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.bImportarXls = QtWidgets.QPushButton(self.groupBox_3)
        self.bImportarXls.setGeometry(QtCore.QRect(10, 30, 131, 51))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/recursos/xls.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bImportarXls.setIcon(icon5)
        self.bImportarXls.setIconSize(QtCore.QSize(32, 32))
        self.bImportarXls.setObjectName("bImportarXls")
        self.bExportarXls = QtWidgets.QPushButton(self.groupBox_3)
        self.bExportarXls.setGeometry(QtCore.QRect(10, 100, 131, 51))
        self.bExportarXls.setIcon(icon5)
        self.bExportarXls.setIconSize(QtCore.QSize(32, 32))
        self.bExportarXls.setObjectName("bExportarXls")
        self.groupBox_4 = QtWidgets.QGroupBox(self.add)
        self.groupBox_4.setGeometry(QtCore.QRect(470, 289, 151, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.bInformePdf = QtWidgets.QPushButton(self.groupBox_4)
        self.bInformePdf.setGeometry(QtCore.QRect(10, 30, 131, 51))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/recursos/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bInformePdf.setIcon(icon6)
        self.bInformePdf.setIconSize(QtCore.QSize(32, 32))
        self.bInformePdf.setObjectName("bInformePdf")
        self.groupBox_5 = QtWidgets.QGroupBox(self.add)
        self.groupBox_5.setGeometry(QtCore.QRect(260, 70, 171, 391))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lwPropietarios = QtWidgets.QListWidget(self.groupBox_5)
        self.lwPropietarios.setGeometry(QtCore.QRect(10, 40, 151, 271))
        self.lwPropietarios.setObjectName("lwPropietarios")
        self.bAddPropietario = QtWidgets.QPushButton(self.groupBox_5)
        self.bAddPropietario.setGeometry(QtCore.QRect(10, 320, 151, 51))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/recursos/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAddPropietario.setIcon(icon7)
        self.bAddPropietario.setIconSize(QtCore.QSize(24, 24))
        self.bAddPropietario.setObjectName("bAddPropietario")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label_11.setObjectName("label_11")
        self.groupBox_6 = QtWidgets.QGroupBox(self.add)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 70, 181, 251))
        self.groupBox_6.setObjectName("groupBox_6")
        self.bAddJuego = QtWidgets.QPushButton(self.groupBox_6)
        self.bAddJuego.setGeometry(QtCore.QRect(10, 180, 161, 51))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/recursos/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAddJuego.setIcon(icon8)
        self.bAddJuego.setIconSize(QtCore.QSize(32, 32))
        self.bAddJuego.setObjectName("bAddJuego")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 141, 141))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/recursos/logo_dados.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.add, "")
        self.bSalir = QtWidgets.QPushButton(self.centralwidget)
        self.bSalir.setGeometry(QtCore.QRect(790, 600, 81, 21))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/recursos/salida.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bSalir.setIcon(icon9)
        self.bSalir.setIconSize(QtCore.QSize(20, 20))
        self.bSalir.setObjectName("bSalir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuBase_de_Datos = QtWidgets.QMenu(self.menuHerramientas)
        self.menuBase_de_Datos.setObjectName("menuBase_de_Datos")
        self.menuXLS = QtWidgets.QMenu(self.menuHerramientas)
        self.menuXLS.setObjectName("menuXLS")
        self.menuInformes = QtWidgets.QMenu(self.menubar)
        self.menuInformes.setObjectName("menuInformes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/arrow_up [#273].png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon10)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionImportarBD = QtWidgets.QAction(MainWindow)
        self.actionImportarBD.setObjectName("actionImportarBD")
        self.actionExportarBD = QtWidgets.QAction(MainWindow)
        self.actionExportarBD.setObjectName("actionExportarBD")
        self.actionEliminarBD = QtWidgets.QAction(MainWindow)
        self.actionEliminarBD.setObjectName("actionEliminarBD")
        self.actionImprimirPdf = QtWidgets.QAction(MainWindow)
        self.actionImprimirPdf.setObjectName("actionImprimirPdf")
        self.actionImportarXls = QtWidgets.QAction(MainWindow)
        self.actionImportarXls.setObjectName("actionImportarXls")
        self.actionExportarXls = QtWidgets.QAction(MainWindow)
        self.actionExportarXls.setObjectName("actionExportarXls")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuBase_de_Datos.addAction(self.actionImportarBD)
        self.menuBase_de_Datos.addAction(self.actionExportarBD)
        self.menuBase_de_Datos.addAction(self.actionEliminarBD)
        self.menuXLS.addAction(self.actionImportarXls)
        self.menuXLS.addAction(self.actionExportarXls)
        self.menuHerramientas.addAction(self.menuBase_de_Datos.menuAction())
        self.menuHerramientas.addAction(self.menuXLS.menuAction())
        self.menuInformes.addAction(self.actionImprimirPdf)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuInformes.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.twListadoJuegos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cod"))
        item = self.twListadoJuegos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.twListadoJuegos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Genero"))
        item = self.twListadoJuegos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dificultad"))
        item = self.twListadoJuegos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Min. Jug."))
        item = self.twListadoJuegos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Max. Jug."))
        item = self.twListadoJuegos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Propietario"))
        item = self.twListadoJuegos.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fecha Alta"))
        self.label_2.setText(_translate("MainWindow", "Listado De Juegos"))
        self.groupBox.setTitle(_translate("MainWindow", "Filtrar"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_3.setText(_translate("MainWindow", "Genero"))
        self.label_4.setText(_translate("MainWindow", "Dificultad"))
        self.label_5.setText(_translate("MainWindow", "Jugadores"))
        self.label_7.setText(_translate("MainWindow", "Min."))
        self.label_6.setText(_translate("MainWindow", "Max."))
        self.label_10.setText(_translate("MainWindow", "Propietario"))
        self.bReiniciarFiltros.setText(_translate("MainWindow", "Reiniciar"))
        self.bFiltrar.setText(_translate("MainWindow", "Filtrar"))
        self.label_12.setText(_translate("MainWindow", "- doble click para ver juego -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.listado), _translate("MainWindow", "Listado"))
        self.label_8.setText(_translate("MainWindow", "Opciones"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Gestion de BD"))
        self.bImportarBD.setText(_translate("MainWindow", "Importar BD"))
        self.bExportarBD.setText(_translate("MainWindow", "Exportar XLS"))
        self.bEliminarBD.setText(_translate("MainWindow", "Eliminar BD"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Archivos XLS"))
        self.bImportarXls.setText(_translate("MainWindow", "Importar XLS"))
        self.bExportarXls.setText(_translate("MainWindow", "Exportar XLS"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Informes"))
        self.bInformePdf.setText(_translate("MainWindow", "Imprimir PDF"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Gestión Propietarios"))
        self.bAddPropietario.setText(_translate("MainWindow", "Añadir Propietarios"))
        self.label_11.setText(_translate("MainWindow", "doble click para eliminar"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Juegos"))
        self.bAddJuego.setText(_translate("MainWindow", "Añadir Juego"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), _translate("MainWindow", "Opciones"))
        self.bSalir.setText(_translate("MainWindow", "SALIR"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.menuBase_de_Datos.setTitle(_translate("MainWindow", "Base de Datos"))
        self.menuXLS.setTitle(_translate("MainWindow", "XLS"))
        self.menuInformes.setTitle(_translate("MainWindow", "Informes"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionImportarBD.setText(_translate("MainWindow", "Importar"))
        self.actionExportarBD.setText(_translate("MainWindow", "Exportar"))
        self.actionEliminarBD.setText(_translate("MainWindow", "Eliminar"))
        self.actionImprimirPdf.setText(_translate("MainWindow", "Pdf"))
        self.actionImportarXls.setText(_translate("MainWindow", "Importar"))
        self.actionExportarXls.setText(_translate("MainWindow", "Exportar"))
import iconos_rc
