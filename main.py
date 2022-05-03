import sys, var
from PyQt5 import QtCore, QtGui, QtWidgets

from constructor import Constructor
from database import Database

if __name__ == '__main__':
    var.db = Database()
    app = QtWidgets.QApplication([])

    var.db.connect()
    Constructor.cargarComponentes()

    Constructor.cargarFiltros()
    Constructor.cargarListadoJuegos()


    Constructor.cargarEventos()

    var.wMain.show()
    sys.exit(app.exec())
