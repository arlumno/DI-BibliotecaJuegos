import os.path
import shutil
import zipfile
import xlrd
import sys

from PyQt5 import QtWidgets

import cargador
import var
from ClasesComponentes import *
from Herramientas import Herramientas


class Acciones():

    def salir():
        try:
            var.dSalir.show()
            if var.dSalir.exec():
                sys.exit()
            else:
                var.dSalir.hide()
        except Exception as error:
            print("Acciones-> error s%:" % str(error))

    def filtrarListado():
        try:
            filtros = {}
            filtros["nombre"] = var.wMain.ui.etNombre.text()
            if not var.wMain.ui.cbGenero.currentText() == "":
                filtros["genero"] = var.wMain.ui.cbGenero.currentText()
            if not var.wMain.ui.cbDificultad.currentText() == "":
                for dificultad in var.db.listadoDificultades().values():
                    if var.wMain.ui.cbDificultad.currentText() == dificultad.dificultad :
                        filtros["dificultad"] = dificultad.id
            if not var.wMain.ui.cbMinJugadores.currentText() == "":
                filtros["min_jugadores"] = var.wMain.ui.cbMinJugadores.currentText()
            if not var.wMain.ui.cbMaxJugadores.currentText() == "":
                filtros["max_jugadores"] = var.wMain.ui.cbMaxJugadores.currentText()
            if not var.wMain.ui.cbPropietario.currentText() == "":
                for propietario in var.db.listadoPropietarios().values():
                    if var.wMain.ui.cbPropietario.currentText() == propietario.nombre:
                        filtros["propietario"] = propietario.id
            cargador.Cargador.cargarListadoJuegos(var.db.listadoJuegosFiltrado(filtros))
        except Exception as error:
            print("Acciones-> error filtrarListado s%:" % str(error))

    def reiniciarFiltros():
        try:
            var.wMain.ui.etNombre.setText("")
            var.wMain.ui.cbGenero.setCurrentText("")
            var.wMain.ui.cbDificultad.setCurrentText("")
            var.wMain.ui.cbMinJugadores.setCurrentText("")
            var.wMain.ui.cbMaxJugadores.setCurrentText("")
            var.wMain.ui.cbPropietario.setCurrentText("")
            var.wMain.ui.cbGenero.setCurrentText("")
            var.wMain.ui.cbGenero.setCurrentText("")
            cargador.Cargador.cargarListadoJuegos()
        except Exception as error:
            print("Acciones-> error reiniciarFiltros s%:" % str(error))

    def abrirJuegoSeleccionado():
        try:
            rowJuego = var.wMain.ui.twListadoJuegos.selectedIndexes()[0].row()
            idJuego = var.rowIdJuegos[rowJuego]
            Acciones.abrirJuego(idJuego)
        except Exception as error:
            print("Acciones-> error abrirJuegoSeleccionado s%:" % str(error))

    def abrirJuego(idJuego):
        try:
            var.dJuego.hide()
            cargador.Cargador.cargarJuego(idJuego)
            var.dJuego.show()
        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def abrirAddJuego():
        Acciones.restaurarCamposAddJuego()
        var.dAddJuego.hide()
        var.dAddJuego.show()

    def cerrarAddJuego():
        try:
            var.dAddJuego.hide()
            Acciones.restaurarCamposAddJuego()
        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def aplicarGenero(genero):
        try:
            var.dAddJuego.ui.etGenero.setText(genero)
            var.dAddJuego.ui.cbGenero.setCurrentText("")
        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def guardarJuego():
        try:
            if var.dAddJuego.ui.etNombre.text() == "":
                Herramientas.ventanaAdvertencia("El campo 'Nombre' es obligatorio")
            else:
                nombre = var.dAddJuego.ui.etNombre.text()
                minJugadores = var.dAddJuego.ui.sbMinJugadores.value()
                maxJugadores = var.dAddJuego.ui.sbMaxJugadores.value()
                id = var.dAddJuego.ui.etCod.text()
                juego = Juego(id, nombre, minJugadores, maxJugadores)
                juego.genero = var.dAddJuego.ui.etGenero.text()
                if not var.dAddJuego.ui.cbDificultad.currentText() == "":
                    juego.dificultad = var.dificultadesByDificultad[str(var.dAddJuego.ui.cbDificultad.currentText())]

                if not var.dAddJuego.ui.cbPropietario.currentText() == "":
                    juego.propietario = var.propietariosByNombre[str(var.dAddJuego.ui.cbPropietario.currentText())]

                juego.descripcion = var.dAddJuego.ui.teDescripcion.toPlainText()
                juego.observaciones = var.dAddJuego.ui.teObservaciones.toPlainText()

                var.db.guardarJuego(juego)
                Acciones.cerrarAddJuego()
                cargador.Cargador.cargarListadoJuegos()
                cargador.Cargador.cargarUI()

        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def editarJuegoAbierto():
        try:
            var.dJuego.hide()
            Acciones.restaurarCamposAddJuego()
            id = var.dJuego.ui.lbCod.text()
            cargador.Cargador.cargarEditarJuego(id)
            var.dAddJuego.hide()
            var.dAddJuego.show()
        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def eliminarJuegoAbierto():
        try:
            id = var.dJuego.ui.lbCod.text()
            nombre = var.dJuego.ui.lbNombre.text()
            juego = Juego(id,nombre)
            if Acciones.eliminarJuego(juego):
                var.dJuego.hide()

        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def eliminarJuego(juego):
        try:
            if Herramientas.ventanaConfirmacion("¿Estas seguro de Eliminar el juego "+juego.nombre+"?", "¡Atención!"):
                var.db.eliminarJuego(juego)
                cargador.Cargador.cargarUI()
                return True
            else:
                return False
        except Exception as error:
            print("Acciones-> error --- s%:" % str(error))

    def addPropietario():
        try:
            if var.dAddPropietario.ui.etNombre.text() != "":
                propietario = Propietario(None,str(var.dAddPropietario.ui.etNombre.text()))
                print(propietario.nombre)
                var.db.guardarPropietario(propietario)
                var.dAddPropietario.hide()
                cargador.Cargador.cargarUIPropietarios()
        except Exception as error:
            print("Acciones-> error addPropietario s%:" % str(error))

    def eliminarPropietario(campo):
        try:
            nombre = campo.text()
            if Herramientas.ventanaConfirmacion("¿Estas seguro de Eliminar el propietario "+nombre+"?", "¡Atención!"):
                propietario = Propietario(None, nombre)
                var.db.eliminarPropietario(propietario)
                cargador.Cargador.cargarUI()
        except Exception as error:
            print("Acciones-> error eliminarPropietario s%:" % str(error))


    def restaurarCamposAddJuego():
        try:
            var.dAddJuego.ui.etNombre.setText("")
            var.dAddJuego.ui.sbMinJugadores.setValue(1)
            var.dAddJuego.ui.sbMaxJugadores.setValue(1)
            var.dAddJuego.ui.etGenero.setText("")
            var.dAddJuego.ui.cbDificultad.setCurrentText("")
            var.dAddJuego.ui.cbPropietario.setCurrentText("")
            var.dAddJuego.ui.teDescripcion.setPlainText("")
            var.dAddJuego.ui.teObservaciones.setPlainText("")
            var.dAddJuego.ui.lbTitulo.setText("Añadir Nuevo Juego")
            var.dAddJuego.ui.lbCod.setVisible(False)
            var.dAddJuego.ui.etCod.setVisible(False)
            var.dAddJuego.ui.etCod.setText("")

        except Exception as error:
            print("Acciones-> error restaurarCamposAddJuego s%:" % str(error))


    def importarXls():
        try:
            dirName, fileName = var.dFileOpen.getOpenFileName(None, None, None, "*.xls *.XLS", )
            if fileName != "":
                archivoXls = xlrd.open_workbook(dirName)
                hoja1 = archivoXls.sheet_by_index(0)
                if hoja1.nrows > 0 and hoja1.ncols >0:
                    #cabeceras
                    #localizamos el indice de cada columna respecto
                    index = {}
                    for i in range(hoja1.ncols):
                        cabecera = str(hoja1.cell_value(0,i)).lower()
                        if cabecera == "nombre": index[i] = "nombre"
                        elif cabecera == "genero": index[i] = "genero"
                        elif cabecera == "dificultad": index[i] = "dificultad"
                        elif cabecera == "min_jugadores": index[i] = "minJugadores"
                        elif cabecera == "max_jugadores": index[i] = "maxJugadores"
                        elif cabecera == "descripcion": index[i] = "descripcion"
                        elif cabecera == "observaciones": index[i] = "observaciones"
                        elif cabecera == "propietario": index[i] = "propietario"
                        elif cabecera == "fecha_alta": index[i] = "fecha_alta"
                    #campos obligatorios
                    if "nombre" not in index.values() or "minJugadores" not in index.values() or "maxJugadores" not in index.values():
                        Herramientas.ventanaAdvertencia("Faltan campos obligatorios en el archivo.")

                    else:
                        listadoJuegos = []
                        dificultades = var.db.listadoDificultades()

                        for e in range(1, hoja1.nrows): #itero cada linea y extraigo sus datos
                            campos = {"nombre":"", "minJugadores":"", "maxJugadores":"", "genero":"", "dificultad":"", "descripcion":"", "observaciones":"", "propietario":"", "fechaAlta":"",}
                            for i in index:
                                if hoja1.cell_type(e,i) == xlrd.XL_CELL_NUMBER:
                                    campos[index[i]] = str(int(hoja1.cell_value(e,i)))
                                else:
                                    campos[index[i]] = str(hoja1.cell_value(e,i))
                            juego = Juego(None,campos["nombre"],campos["minJugadores"],campos["maxJugadores"])
                            juego.genero = campos["genero"]
                            juego.descripcion = campos["descripcion"]
                            juego.observaciones = campos["observaciones"]
                            juego.fechaAlta = campos["fechaAlta"]
                            if not campos["dificultad"] == "":
                                juego.dificultad = dificultades[campos["dificultad"]]

                            if not campos["propietario"] == "":
                                if campos["propietario"] in var.propietariosByNombre.keys():
                                    juego.propietario = var.propietariosByNombre[campos["propietario"]]
                                else:
                                    juego.propietario = Propietario(None,campos["propietario"])
                            # print(juego)
                            listadoJuegos.append(juego)

                        Acciones.importarJuegos(listadoJuegos)

                else:
                    Herramientas.ventanaAdvertencia("No hay datos para importar en el archivo")

        except Exception as error:
            print("Acciones-> error importarXls s%:" % str(error))

    def importarJuegos(listadoJuegos):
        try:
            listaStr = ""
            for juego in listadoJuegos:
                listaStr = listaStr + str(juego.nombre) + "\n"
            if Herramientas.ventanaConfirmacion("Hay un total de " + str(
                    len(listadoJuegos)) + " Juegos para importar. Los Juegos existentes se actualizarán. \n¿Está seguro?",
                                                "Importar Juegos", None, listaStr
                                                ):
                var.db.guardarListadoJuegos(listadoJuegos)
                cargador.Cargador.cargarUI()
        except Exception as error:
            print("Acciones-> error importarJuegos s%:" % str(error))

    def eliminarBD():
        try:
            if Herramientas.ventanaConfirmacion("¿Estas seguro de Eliminar todos los registros de la Base De Datos?", "¡Atención!"):
                if var.db.eliminarBD():
                    Acciones.anunciarStatusBar("Se han eliminado todos los registros.")

                cargador.Cargador.cargarUI()
        except Exception as error:
            print("Acciones-> error eliminarBD s%:" % str(error))

    def exportarBD():
        try:
            archivoSalida = str(Herramientas.fechaActual('%Y.%m.%d.%H.%M.%S')) + '_copia.zip'
            option = QtWidgets.QFileDialog.Options()
            directorio, archivo = var.dFileOpen.getSaveFileName(None,"Descargar Copia",archivoSalida, '.zip', options=option)
            if var.dFileOpen.Accepted and archivo != '':
                archivoZip = zipfile.ZipFile(archivoSalida,'w')
                archivoZip.write(var.db.fileDb, os.path.basename(var.db.fileDb),zipfile.ZIP_DEFLATED)
                archivoZip.close()
                Acciones.anunciarStatusBar("Base de datos exportada con éxito")
                shutil.move(str(archivoSalida),str(directorio))
        except Exception as error:
                print("Acciones-> error exportarBD s%:" % str(error))

    def importarBD():
        try:
            dirName, fileName = var.dFileOpen.getOpenFileName(None,None,None,"*.zip *.ZIP",)

            if dirName and Herramientas.ventanaConfirmacion("¿Estas seguro de impotar la BD? Se perderán los datos actuales","¡Atención!",None,dirName):
                archivoZip = zipfile.ZipFile(dirName, 'r')

                var.db.disconnect()  #desconectamos para poder renombrar la base de datos actual
                os.replace(var.db.fileDb, var.db.fileDbBackup) #le cambiamos el nombre y la dejamos como copia de seguridad

                try:
                    archivoZip.extract(var.db.fileDb) #extraemos la base de datos del archivo zip.
                    var.db.connect() #conectamos de nuevo la bd.
                    Acciones.anunciarStatusBar("Base de datos restaurada")
                    Herramientas.ventanaAdvertencia("Base de datos restaurada con éxito.")
                except Exception as error: #si da error, deshacemos el cambio.
                    os.replace(var.db.fileDbBackup, var.db.fileDb)  # le cambiamos el nombre y la dejamos como copia de seguridad
                    var.db.connect() #conectamos de nuevo la bd.
                    Acciones.anunciarStatusBar("No se ha podido importar la Base de datos","error",str(error))
                    Herramientas.ventanaAdvertencia("No se ha podido importar la Base de datos","error",str(error))

                cargador.Cargador.cargarUI()

        except Exception as error:
            print("Acciones-> error importarBD s%:" % str(error))

    def anunciarStatusBar(msg):
        try:
            var.wMain.ui.lbStatus.setText("[" + Herramientas.fechaActual("%d/%m/%Y %H:%M:%S") + "] " + msg)
        except Exception as error:
            print("Acciones-> error anunciarStatusBar s%:" % str(error))

