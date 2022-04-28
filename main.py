import sys, var

from UiPrincipal import *
from ClasesUi import *
from Acciones import Acciones
from Database import Database
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import informes

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.menu = Ui_MainWindow()
        var.menu.setupUi(self)

        var.dSalir = DialogSalir()
        var.dCalendar = DialogCalendar()
        var.dLog = DialogLog()
        var.dFileOpen = FileDialogAbrir()

        # var.dLog.show()
        # database.Database.connect()

        # Acciones.cargarProvincias()
        # Acciones.cargarEnvios()
        # Acciones.cargarClientes()
        # Acciones.limpiarCamposCliente()
        # var.menu.statusbar.addPermanentWidget(var.menu.lbStatus,1)
        # Acciones.anunciarStatusBar("Bienvenido a 2º DAM - Adultos")
        # var.menu.bAceptar.setVisible(False) #Lo oculto porque no lo estoy usando para nada actualmente.
        # var.menu.sbEnvio.setMinimum(0)
        # var.menu.sbEnvio.setMaximum(len(var.listadoEnvios) - 1)
        # var.menu.sbEnvio.setValue(0)
        # var.menu.etEnvio.setText(var.listaEnvio[0])
        # Acciones.addToLog("prueba de texto 1")
        # Acciones.addToLog("prueba de texto 2")

        ### EVENTOS ###
        # var.menu.cbProvincia.activated[str].connect(Acciones.selProvincia)

        # var.menu.tablaDatos.selectionModel().selectionChanged.connect(Acciones.modificarCliente)
        # var.menu.tablaDatos.doubleClicked.connect(Acciones.abrirClienteSeleccionado)
        # print(var.menu.tablaDatos.selectedIndexes())

        #Botones
        var.menu.bSalir.clicked.connect(Acciones.salir)
        # var.menu.bCargarClientes.clicked.connect(Acciones.cargarClientes)
        # var.menu.bFiltrarClientes.clicked.connect(Acciones.filtrarClientes)
        # var.menu.etFiltro.editingFinished.connect(Acciones.filtrarClientes)
        # var.menu.bLimpiarClientes.clicked.connect(Acciones.limpiarListadoClientes)
        # var.menu.bEliminarClienteSeleccionado.clicked.connect(Acciones.eliminarClienteSeleccionado)
        # var.menu.bEliminarCliente.clicked.connect(Acciones.eliminarCliente)
        # var.menu.bModificarCliente.clicked.connect(Acciones.abrirClienteSeleccionado)
        # var.menu.bGuardarCambios.clicked.connect(Acciones.guardarCambiosCliente)
        # var.menu.bNuevoCliente.clicked.connect(Acciones.grabarNuevoCliente)
        # var.menu.bLimpiarCampos.clicked.connect(Acciones.limpiarCamposCliente)
        # var.menu.etDni.editingFinished.connect(Acciones.comprobarCampoDni)
        # var.menu.sbEnvio.valueChanged.connect(Acciones.asignarEnvio)



        #Actions menú
        # var.menu.actionSalir.triggered.connect(Acciones.salir)
        # var.menu.actionLog.triggered.connect(Acciones.abrirLog)
        # var.menu.actionAbrirCarpeta.triggered.connect(Acciones.abrirCarpeta)
        # var.menu.actionDescargarBd.triggered.connect(Acciones.descargarBd)
        # var.menu.actionRestaurarBD.triggered.connect(Acciones.restaurarBd)
        # var.menu.actionBorrarBD.triggered.connect(Acciones.borrarClientesBd)
        # var.menu.actionImportar_Datos.triggered.connect(Acciones.importarDatos)
        # var.menu.actionGenerarInformeClientes.triggered.connect(informes.Informes.reportCli)

        #radiobuttons y checkboxs
        # var.menu.rbgSexo.buttonClicked.connect(Acciones.selSexo)
        # # var.menu.rbFemenino.toggled.connect(Acciones.selSexo)
        # # var.menu.rbMasculino.toggled.connect(Acciones.selSexo)
        # var.menu.chkEfectivo.stateChanged.connect(Acciones.selPago)
        # var.menu.chkTarjeta.stateChanged.connect(Acciones.selPago)
        # var.menu.chkTransfer.stateChanged.connect(Acciones.selPago)
        #
        # var.menu.bCalendar.clicked.connect(Acciones.abrirCalendar)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    wMain = Main()
    wMain.show()
    #var.dLog.show() #en proceso
    # Acciones.addToLog()
    sys.exit(app.exec())

