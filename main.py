import sys, var
from PyQt5 import QtCore, QtGui, QtWidgets

from cargador import Cargador
from database import Database

if __name__ == '__main__':
    try:
        var.db = Database()
        app = QtWidgets.QApplication([])

        var.db.connect()
        Cargador.cargarComponentes()

        Cargador.cargarUI()
        Cargador.cargarEventos()

        var.wMain.show()
        sys.exit(app.exec())
    except Exception as error:
        print("error addPropietario s%:" % str(error))

