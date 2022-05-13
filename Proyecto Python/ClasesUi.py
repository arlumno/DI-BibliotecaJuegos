import sys
from datetime import datetime

from UiDialogAddJuego import Ui_DialogAddJuego
from UiDialogAddPropietario import Ui_DialogAddPropietario
from UiDialogJuego import Ui_DialogJuego
from UiPrincipal import *
from UiDialogSalir import *


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #este metodo sobreescrito permite cerrar la aplicación por completo al cerrar la ventana de main en el boton superior izquierdo X
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("exit")
        sys.exit()

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        self.ui = Ui_DialogSalir()
        self.ui.setupUi(self)

class DialogAddPropietario(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAddPropietario, self).__init__()
        self.ui = Ui_DialogAddPropietario()
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