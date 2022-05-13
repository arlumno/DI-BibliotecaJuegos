import sys, var
from PyQt5 import QtCore, QtGui, QtWidgets

from cargador import Cargador
from database import Database

if __name__ == '__main__':
    var.db = Database()
    app = QtWidgets.QApplication([])

    #carga todas las ventanas
    Cargador.cargarComponentes()

    #conecta la base de datos
    var.db.connect()

    #carga todos los datos en los campos de todas las ventanas
    Cargador.cargarUI()
    #carga todos los eventos asociados a botones, campos..
    Cargador.cargarEventos()

    #muestra la ventana principal
    var.wMain.show()

    sys.exit(app.exec())
