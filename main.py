import sys, var
from PyQt5 import QtCore, QtGui, QtWidgets

from Constructor import Constructor
from Database import Database
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import informes

if __name__ == '__main__':
    var.db = Database()
    app = QtWidgets.QApplication([])

    var.db.connect()
    Constructor.cargarComponentes()
    Constructor.cargarPropietarios()
    Constructor.cargarDificultades()

    Constructor.cargarEventos()

    var.wMain.show()
    sys.exit(app.exec())
