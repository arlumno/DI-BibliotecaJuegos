import sys, var
from PyQt5 import QtCore, QtGui, QtWidgets

from cargador import Cargador
from database import Database

if __name__ == '__main__':
    var.db = Database()
    app = QtWidgets.QApplication([])

    Cargador.cargarComponentes()

    var.db.connect()

    Cargador.cargarUI()
    Cargador.cargarEventos()
    var.wMain.show()

    sys.exit(app.exec())
