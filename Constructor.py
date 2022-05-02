import var
from ClasesUi import *
from Acciones import Acciones



class Constructor():

    def cargarComponentes():
        # cargar UI principal.
        var.wMain = Main()

        # cargar UIs adicionales.
        var.dSalir = DialogSalir()
        # var.dCalendar = DialogCalendar()
        var.dLog = DialogLog()
        var.dFileOpen = FileDialogAbrir()

    def cargarEventos():
        var.wMain.ui.bSalir.clicked.connect(Acciones.salir)
        var.wMain.ui.bFiltrar.clicked.connect(Acciones.filtrarListado)



    def cargarListadoJuegos(listadoJuegos):
        var.wMain.ui.twListadoJuegos.setRowCount(0)
        if len(listadoJuegos) > 0:
            row = 0
            for juego in listadoJuegos:
                var.wMain.ui.twListadoJuegos.insertRow(row)
                var.wMain.ui.twListadoJuegos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(juego.id)))
                var.wMain.ui.twListadoJuegos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(juego.nombre)))
                var.wMain.ui.twListadoJuegos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(juego.genero)))
                var.wMain.ui.twListadoJuegos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(juego.dificultad.dificultad)))
                var.wMain.ui.twListadoJuegos.setItem(row, 4, QtWidgets.QTableWidgetItem(str(juego.minJugadores)))
                var.wMain.ui.twListadoJuegos.setItem(row, 5, QtWidgets.QTableWidgetItem(str(juego.maxJugadores)))
                var.wMain.ui.twListadoJuegos.setItem(row, 6, QtWidgets.QTableWidgetItem(str(juego.propietario.nombre)))
                var.wMain.ui.twListadoJuegos.setItem(row, 7, QtWidgets.QTableWidgetItem(str(juego.fechaAlta)))
                row += 1

    def cargarFiltros():
        Constructor.cargarFiltroPropietarios()
        Constructor.cargarFiltroDificultades()


    def cargarFiltroPropietarios():
        try:
            var.wMain.ui.cbPropietario.addItem("")
            for i in var.db.listadoPropietarios().values():
                var.wMain.ui.cbPropietario.addItem(i.nombre)
        except Exception as error:
            print("Error al cargar propietarios: " + str(error))

    def cargarFiltroDificultades():
        try:
            var.wMain.ui.cbDificultad.addItem("")
            for i in var.db.listadoDificultades().values():
                var.wMain.ui.cbDificultad.addItem(i.dificultad)
        except Exception as error:
            print("Error al cargar dificultades: " + str(error))