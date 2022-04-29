import var
from ClasesUi import *
from Acciones import Acciones



class Constructor():

    def cargarComponentes():
        var.wMain = Main()
        # cargar UIs adicionales.
        var.dSalir = DialogSalir()

        # var.dCalendar = DialogCalendar()
        var.dLog = DialogLog()
        var.dFileOpen = FileDialogAbrir()
        # var.dLog.show()

    def cargarEventos():
        var.wMain.ui.bSalir.clicked.connect(Acciones.salir)

    def cargarPropietarios():
        try:
            for i in var.db.listadoPropietarios():
                var.wMain.ui.cbPropietario.addItem(i.nombre)
        except Exception as error:
            print("Error al cargar propietarios: " + str(error))

    def cargarDificultades():
        try:
            for i in var.db.listadoDificultades():
                var.wMain.ui.cbDificultad.addItem(i.dificultad)
        except Exception as error:
            print("Error al cargar dificultades: " + str(error))