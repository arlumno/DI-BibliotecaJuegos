from datetime import datetime

from UiDialogAddJuego import Ui_DialogAddJuego
from UiDialogJuego import Ui_DialogJuego
from UiPrincipal import *
from UiDialogSalir import *
from UiDialogLog import *
# from UiDialogCalendar import *


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Acciones.cargarEnvios()
        # Acciones.cargarClientes()
        # Acciones.limpiarCamposCliente()
        # self.ui.statusbar.addPermanentWidget(self.ui.lbStatus,1)
        # Acciones.anunciarStatusBar("Bienvenido a 2º DAM - Adultos")
        # self.ui.bAceptar.setVisible(False) #Lo oculto porque no lo estoy usando para nada actualmente.
        # self.ui.sbEnvio.setMinimum(0)
        # self.ui.sbEnvio.setMaximum(len(var.listadoEnvios) - 1)
        # self.ui.sbEnvio.setValue(0)
        # self.ui.etEnvio.setText(var.listaEnvio[0])
        # Acciones.addToLog("prueba de texto 1")
        # Acciones.addToLog("prueba de texto 2")

        ### EVENTOS ###
        # self.ui.cbProvincia.activated[str].connect(Acciones.selProvincia)

        # self.ui.tablaDatos.selectionModel().selectionChanged.connect(Acciones.modificarCliente)
        # self.ui.tablaDatos.doubleClicked.connect(Acciones.abrirClienteSeleccionado)
        # print(self.ui.tablaDatos.selectedIndexes())

        #Botones
        # self.ui.bCargarClientes.clicked.connect(Acciones.cargarClientes)
        # self.ui.bFiltrarClientes.clicked.connect(Acciones.filtrarClientes)
        # self.ui.etFiltro.editingFinished.connect(Acciones.filtrarClientes)
        # self.ui.bLimpiarClientes.clicked.connect(Acciones.limpiarListadoClientes)
        # self.ui.bEliminarClienteSeleccionado.clicked.connect(Acciones.eliminarClienteSeleccionado)
        # self.ui.bEliminarCliente.clicked.connect(Acciones.eliminarCliente)
        # self.ui.bModificarCliente.clicked.connect(Acciones.abrirClienteSeleccionado)
        # self.ui.bGuardarCambios.clicked.connect(Acciones.guardarCambiosCliente)
        # self.ui.bNuevoCliente.clicked.connect(Acciones.grabarNuevoCliente)
        # self.ui.bLimpiarCampos.clicked.connect(Acciones.limpiarCamposCliente)
        # self.ui.etDni.editingFinished.connect(Acciones.comprobarCampoDni)
        # self.ui.sbEnvio.valueChanged.connect(Acciones.asignarEnvio)



        #Actions menú
        # self.ui.actionSalir.triggered.connect(Acciones.salir)
        # self.ui.actionLog.triggered.connect(Acciones.abrirLog)
        # self.ui.actionAbrirCarpeta.triggered.connect(Acciones.abrirCarpeta)
        # self.ui.actionDescargarBd.triggered.connect(Acciones.descargarBd)
        # self.ui.actionRestaurarBD.triggered.connect(Acciones.restaurarBd)
        # self.ui.actionBorrarBD.triggered.connect(Acciones.borrarClientesBd)
        # self.ui.actionImportar_Datos.triggered.connect(Acciones.importarDatos)
        # self.ui.actionGenerarInformeClientes.triggered.connect(informes.Informes.reportCli)

        #radiobuttons y checkboxs
        # self.ui.rbgSexo.buttonClicked.connect(Acciones.selSexo)
        # # self.ui.rbFemenino.toggled.connect(Acciones.selSexo)
        # # self.ui.rbMasculino.toggled.connect(Acciones.selSexo)
        # self.ui.chkEfectivo.stateChanged.connect(Acciones.selPago)
        # self.ui.chkTarjeta.stateChanged.connect(Acciones.selPago)
        # self.ui.chkTransfer.stateChanged.connect(Acciones.selPago)
        #
        # self.ui.bCalendar.clicked.connect(Acciones.abrirCalendar)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        self.ui = Ui_DialogSalir()
        self.ui.setupUi(self)


# class DialogCalendar(QtWidgets.QDialog):
#     def __init__(self):
#         super(DialogCalendar, self).__init__()
#         self.ui = Ui_DialogCalendar()
#         self.ui.setupUi(self)
#         diaHoy = datetime.now().day
#         mesHoy = datetime.now().month
#         anhoHoy = datetime.now().year
#
#         self.ui.calendarWidget.setSelectedDate(QtCore.QDate(anhoHoy, mesHoy, diaHoy))
#         self.ui.calendarWidget.clicked.connect(Acciones.asignarFecha)


class DialogLog(QtWidgets.QDialog):
    def __init__(self):
        super(DialogLog, self).__init__()
        self.ui = Ui_DialogLog()
        self.ui.setupUi(self)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

class DialogJuego(QtWidgets.QDialog):
    def __init__(self):
        super(DialogJuego, self).__init__()
        self.ui = Ui_DialogJuego()
        self.ui.setupUi(self)

class DialogAddJuego(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAddJuego, self).__init__()
        self.ui = Ui_DialogAddJuego()
        self.ui.setupUi(self)