from datetime import datetime
from UiDialogSalir import *
from UiDialogLog import *
from UiDialogCalendar import *
from Acciones import Acciones

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        self.ui = Ui_DialogSalir()
        self.ui.setupUi(self)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        self.ui = Ui_DialogCalendar()
        self.ui.setupUi(self)
        diaHoy = datetime.now().day
        mesHoy = datetime.now().month
        anhoHoy = datetime.now().year

        self.ui.calendarWidget.setSelectedDate(QtCore.QDate(anhoHoy, mesHoy, diaHoy))
        self.ui.calendarWidget.clicked.connect(Acciones.asignarFecha)


class DialogLog(QtWidgets.QDialog):
    def __init__(self):
        super(DialogLog, self).__init__()
        self.ui = Ui_DialogLog()
        self.ui.setupUi(self)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
