import informes
import var
from ClasesUi import *
from acciones import Acciones



class Cargador():

    # carga todas las ventanas en variables globales
    def cargarComponentes():
        try:
            # cargar UI principal.
            var.wMain = Main()
            # cargar UIs adicionales.
            var.dSalir = DialogSalir()
            var.dJuego = DialogJuego()
            var.dAddJuego = DialogAddJuego()
            var.dAddPropietario = DialogAddPropietario()
            var.dFileOpen = FileDialogAbrir()
        except Exception as error:
            print("Cargador-> error cargarComponentes s% " % str(error))

    #asigna eventos y sus acciones a los campos y botones de la UI
    def cargarEventos():
        try:
            #UI Main
            uiMain = var.wMain.ui
            uiMain.bSalir.clicked.connect(Acciones.salir)
            uiMain.bFiltrar.clicked.connect(Acciones.filtrarListado)
            uiMain.bReiniciarFiltros.clicked.connect(Acciones.reiniciarFiltros)
            uiMain.twListadoJuegos.doubleClicked.connect(Acciones.abrirJuegoSeleccionado)
            uiMain.bAddJuego.clicked.connect(Acciones.abrirAddJuego)
            uiMain.bImportarXls.clicked.connect(Acciones.importarXls)
            uiMain.bInformePdf.clicked.connect(informes.Informes.reportCli)
            uiMain.bEliminarBD.clicked.connect(Acciones.eliminarBD)
            uiMain.bExportarBD.clicked.connect(Acciones.exportarBD)
            uiMain.bImportarBD.clicked.connect(Acciones.importarBD)
            uiMain.bAddPropietario.clicked.connect(var.dAddPropietario.show)
            uiMain.lwPropietarios.itemDoubleClicked.connect(Acciones.eliminarPropietario)

            #Barra menu.
            uiMain.actionAddJuego.triggered.connect(Acciones.abrirAddJuego)
            uiMain.actionSalir.triggered.connect(Acciones.salir)
            uiMain.actionImportarXls.triggered.connect(Acciones.importarXls)
            uiMain.actionImprimirPdf.triggered.connect(informes.Informes.reportCli)
            uiMain.actionEliminarBD.triggered.connect(Acciones.eliminarBD)
            uiMain.actionExportarBD.triggered.connect(Acciones.exportarBD)
            uiMain.actionImportarBD.triggered.connect(Acciones.importarBD)

            #Ui Juego
            var.dJuego.ui.bCerrar.clicked.connect(var.dJuego.hide)
            var.dJuego.ui.bEliminar.clicked.connect(Acciones.eliminarJuegoAbierto)
            var.dJuego.ui.bEditar.clicked.connect(Acciones.editarJuegoAbierto)

            #Ui AddJuego
            var.dAddJuego.ui.bCerrar.clicked.connect(Acciones.cerrarAddJuego)
            var.dAddJuego.ui.bGuardar.clicked.connect(Acciones.guardarJuego)
            var.dAddJuego.ui.cbGenero.activated[str].connect(Acciones.aplicarGenero)
            var.dAddJuego.ui.bAddPropietario.clicked.connect(var.dAddPropietario.show)

            #Ui AddPropietario
            var.dAddPropietario.ui.bGuardar.clicked.connect(Acciones.addPropietario)
            var.dAddPropietario.ui.bCancelar.clicked.connect(var.dAddPropietario.hide);
        except Exception as error:
            print("Cargador-> error cargarEventos s% " % str(error))

    # carga todos los datos en los campos de todas las ventanas
    def cargarUI():
        try:
            #clasificado según datos cargados.
            Cargador.cargarListadoJuegos()
            Cargador.cargarUIGenero()
            Cargador.cargarUIDificultades()
            Cargador.cargarUIMinJugadores()
            Cargador.cargarUIMaxJugadores()
            Cargador.cargarUIPropietarios()
        except Exception as error:
            print("Cargador-> error cargarUI s% " % str(error))

    #carga el listado en el QTableWidget
    def cargarListadoJuegos(listadoJuegos = None):
        try:
            if listadoJuegos is None:
                listadoJuegos = var.db.listadoJuegos()
            var.wMain.ui.twListadoJuegos.setRowCount(0)
            if len(listadoJuegos) > 0:
                row = 0
                var.rowIdJuegos = {}
                for juego in listadoJuegos:
                    var.wMain.ui.twListadoJuegos.insertRow(row)
                    var.wMain.ui.twListadoJuegos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(juego.id)))
                    var.wMain.ui.twListadoJuegos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(juego.nombre)))
                    var.wMain.ui.twListadoJuegos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(juego.genero)))
                    if juego.dificultad is None:
                        var.wMain.ui.twListadoJuegos.setItem(row, 3, QtWidgets.QTableWidgetItem(""))
                    else:
                        var.wMain.ui.twListadoJuegos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(juego.dificultad.dificultad)))

                    var.wMain.ui.twListadoJuegos.setItem(row, 4, QtWidgets.QTableWidgetItem(str(juego.minJugadores)))
                    var.wMain.ui.twListadoJuegos.setItem(row, 5, QtWidgets.QTableWidgetItem(str(juego.maxJugadores)))
                    if juego.propietario is None:
                        var.wMain.ui.twListadoJuegos.setItem(row, 6, QtWidgets.QTableWidgetItem(""))
                    else:
                        var.wMain.ui.twListadoJuegos.setItem(row, 6, QtWidgets.QTableWidgetItem(str(juego.propietario.nombre)))
                    var.wMain.ui.twListadoJuegos.setItem(row, 7, QtWidgets.QTableWidgetItem(str(juego.fechaAlta)))
                    var.rowIdJuegos[row] = juego.id
                    row += 1
        except Exception as error:
            print("Cargador-> error cargarListadoJuegos s% " % str(error))



    def cargarUIDificultades():
        try:
            var.wMain.ui.cbDificultad.clear()
            var.dAddJuego.ui.cbDificultad.clear()

            var.wMain.ui.cbDificultad.addItem("")
            var.dAddJuego.ui.cbDificultad.addItem("")
            for i in var.db.listadoDificultades().values():
                var.wMain.ui.cbDificultad.addItem(i.dificultad)
                var.dAddJuego.ui.cbDificultad.addItem(i.dificultad)
        except Exception as error:
            print("Cargador-> error cargarUIDificultades s% " % str(error))


    def cargarUIPropietarios():
        try:
            var.wMain.ui.cbPropietario.clear()
            var.wMain.ui.lwPropietarios.clear()
            var.dAddJuego.ui.cbPropietario.clear()

            var.wMain.ui.cbPropietario.addItem("")
            var.dAddJuego.ui.cbPropietario.addItem("")
            for i in var.db.listadoPropietarios().values():
                var.wMain.ui.cbPropietario.addItem(i.nombre)
                var.wMain.ui.lwPropietarios.addItem(i.nombre)
                var.dAddJuego.ui.cbPropietario.addItem(i.nombre)

        except Exception as error:
            print("Cargador-> error cargarUIPropietarios s% " % str(error))


    def cargarUIMinJugadores():
        try:
            var.wMain.ui.cbMinJugadores.clear()

            var.wMain.ui.cbMinJugadores.addItem("")
            for i in var.db.listadoMinJugadores():
                var.wMain.ui.cbMinJugadores.addItem(str(i))
        except Exception as error:
            print("Cargador-> error cargarUIMinJugadores s% " % str(error))

    def cargarUIMaxJugadores():
        try:
            var.wMain.ui.cbMaxJugadores.clear()
            var.wMain.ui.cbMaxJugadores.addItem("")
            for i in var.db.listadoMaxJugadores():
                var.wMain.ui.cbMaxJugadores.addItem(str(i))
        except Exception as error:
            print("Cargador-> error cargarUIMaxJugadores s% " % str(error))

    def cargarUIGenero():
        try:
            listadoGeneros = []
            if listadoGeneros.count("") == 0 :
                listadoGeneros = var.db.listadoGeneros()
            var.wMain.ui.cbGenero.clear()
            var.wMain.ui.cbGenero.addItem("")
            var.dAddJuego.ui.cbGenero.addItem("")
            for i in listadoGeneros:
                var.wMain.ui.cbGenero.addItem(str(i))
                var.dAddJuego.ui.cbGenero.addItem(str(i))
        except Exception as error:
            print("Cargador-> error cargarUIGenero s% " % str(error))

    #carga la información de un juego en la ventana dJuego
    def cargarJuego(idJuego):
        try:
            juego = var.db.obtenerJuego(idJuego)
            var.dJuego.hide()
            var.dJuego.ui.lbNombre.setText(juego.nombre)
            if juego.propietario is None:
                var.dJuego.ui.lbPropietario.setText("")
            else:
                var.dJuego.ui.lbPropietario.setText(juego.propietario.nombre)

            if juego.dificultad is None:
                var.dJuego.ui.lbDificultad.setText("")
            else:
                var.dJuego.ui.lbDificultad.setText(juego.dificultad.dificultad)

            var.dJuego.ui.lbGenero.setText(juego.genero)
            var.dJuego.ui.lbNJugadores.setText(str(juego.minJugadores) + " - "+ str(juego.maxJugadores))
            var.dJuego.ui.lbAlta.setText(juego.fechaAlta)
            var.dJuego.ui.lbCod.setText(str(juego.id))
            var.dJuego.ui.teDescripcion.setPlainText(juego.descripcion)
            var.dJuego.ui.teObservaciones.setPlainText(juego.observaciones)
        except Exception as error:
            print("Cargador-> error cargarJuego s% " % str(error))

    #carga la información de un juego en la ventana dAddJuego
    def cargarEditarJuego(idJuego):
        try:
            juego = var.db.obtenerJuego(idJuego)
            var.dAddJuego.hide()
            var.dAddJuego.ui.lbTitulo.setText("Editar Juego")
            var.dAddJuego.ui.lbCod.setVisible(True)
            var.dAddJuego.ui.etCod.setVisible(True)
            var.dAddJuego.ui.etNombre.setText(juego.nombre)
            if juego.propietario is None:
                var.dAddJuego.ui.cbPropietario.setCurrentText("")
            else:
                var.dAddJuego.ui.cbPropietario.setCurrentText(juego.propietario.nombre)

            if juego.dificultad is None:
                var.dAddJuego.ui.cbDificultad.setCurrentText("")
            else:
                var.dAddJuego.ui.cbDificultad.setCurrentText(juego.dificultad.dificultad)

            var.dAddJuego.ui.etGenero.setText(juego.genero)
            var.dAddJuego.ui.sbMinJugadores.setValue(int(juego.minJugadores))
            var.dAddJuego.ui.sbMaxJugadores.setValue(int(juego.maxJugadores))
            var.dAddJuego.ui.etCod.setText(str(juego.id))
            var.dAddJuego.ui.teDescripcion.setPlainText(juego.descripcion)
            var.dAddJuego.ui.teObservaciones.setPlainText(juego.observaciones)

        except Exception as error:
            print("Cargador-> error cargarJuego s% " % str(error))
