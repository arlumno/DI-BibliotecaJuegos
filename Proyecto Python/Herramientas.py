from datetime import datetime

from PyQt5.QtWidgets import QMessageBox


class Herramientas():
    #devuelve la fecha actual, formato por defecto: "%d/%m/%Y"
    def fechaActual(format= "%d/%m/%Y"):
        fecha = datetime.today()
        fecha = fecha.strftime(format)
        return str(fecha)

    #muestra ventana de advertencia con los datos indicados
    def ventanaAdvertencia(mensaje = "", titulo="Atención", descripcion=""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setDetailedText(descripcion)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # muestra ventana de confirmación  con los datos indicados, y los botones de aceptar o cancelar.
    def ventanaConfirmacion(mensaje ="", titulo ="Atención", descripcion ="",descripcionExtendida = ""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setInformativeText(descripcion)
        if descripcionExtendida != "":
            msg.setDetailedText(descripcionExtendida)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            return True
        else:
            return False

