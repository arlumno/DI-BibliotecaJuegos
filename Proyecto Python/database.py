import os.path
import shutil
import sys
import tempfile

from PyQt5 import QtWidgets, QtSql

import var
import acciones
from ClasesComponentes import *
import cargador
from Herramientas import Herramientas


class Database():
    fileDb = "app.db"
    fileDbBackup = "app.db.bk"
    fileDbEmpty = "app.empty.db"
    consultaJuegos = "SELECT id, nombre, min_jugadores, max_jugadores, dificultad, genero, propietario, fecha_alta, descripcion, observaciones FROM juegos"

    def __init__(self):
        self.db = None

    def connect(self):
        if not os.path.isfile(self.fileDb):
            if os.path.isfile(self.fileDbEmpty):
                shutil.copy(self.fileDbEmpty, self.fileDb) #para modo desarrollo
            else:
                shutil.copy(sys._MEIPASS+'/'+self.fileDbEmpty, self.fileDb)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.fileDb)
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, "No se puede abrir la base de datos",
                                           'No se puede establecer conexión.', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            acciones.Acciones.anunciarStatusBar("Conexión a la BD realizada con éxito")
        return True

    def eliminarBD(self):
        self.disconnect()
        os.remove(self.fileDb);
        self.connect()
        return True

    def disconnect(self):
        self.db.close()
        acciones.Acciones.anunciarStatusBar("Base de datos desconectada.")

    def listadoJuegos(self):
        q = QtSql.QSqlQuery()
        q.prepare(self.consultaJuegos)
        listado = []
        if q.exec_():
            listado = self.procesarConsultaJuegos(q)
        else:
            print("DB - Error al obtener listado de juegos: ", q.lastError().text())
        return listado

    def obtenerJuego(self, idJuego):
        q = QtSql.QSqlQuery()
        q.prepare(self.consultaJuegos + " WHERE id = :id")
        q.bindValue(":id",str(idJuego))

        juego = None
        if q.exec_():
            juego = self.procesarConsultaJuegos(q)[0]
        else:
            print("DB - Error al obtener juego: ", q.lastError().text())
        return juego

    def procesarConsultaJuegos(self,q):
        propietarios = self.listadoPropietarios();
        dificultades = self.listadoDificultades();
        listado = []

        while q.next():
            juego = Juego(q.value(0), q.value(1), q.value(2), q.value(3))

            if not q.value(4) == "":
                juego.dificultad = dificultades[str(q.value(4))]

            juego.genero = q.value(5)

            if not q.value(6) == "":
                juego.propietario = propietarios[str(q.value(6))]

            juego.fechaAlta = q.value(7)
            juego.descripcion = q.value(8)
            juego.observaciones = q.value(9)

            listado.append(juego)
        return listado

    def listadoPropietarios(self):
        q = QtSql.QSqlQuery()
        q.prepare("SELECT id, nombre FROM propietarios")
        listado = {}
        propietariosByNombre = {}
        if q.exec_():
            while q.next():
                propietario = Propietario(q.value(0), q.value(1))
                propietariosByNombre[str(q.value(1))] = propietario
                listado[str(q.value(0))] = propietario
        else:
            print("DB - Error al obtener listado de propietarios: ", q.lastError().text())

        var.propietariosByNombre = propietariosByNombre

        return listado

    def listadoDificultades(self):
        q = QtSql.QSqlQuery()
        q.prepare("SELECT id, dificultad FROM dificultad")
        listado = {}
        dificultadesByDificultad = {}
        if q.exec_():
            while q.next():
                dificultad = Dificultad(q.value(0), q.value(1))
                dificultadesByDificultad[str(q.value(1))] = dificultad
                listado[str(q.value(0))] = dificultad
        else:
            print("DB - Error al obtener listado de dificultades: ", q.lastError().text())
        var.dificultadesByDificultad = dificultadesByDificultad
        return listado

    def listadoMinJugadores(self):
        q = QtSql.QSqlQuery()
        q.prepare("SELECT distinct(min_jugadores) FROM juegos ORDER BY min_jugadores")
        listado = []
        if q.exec_():
            while q.next():
                listado.append(q.value(0))
        else:
            print("DB - Error al obtener listado de min jugadores: ", q.lastError().text())

        return listado

    def listadoMaxJugadores(self):
        q = QtSql.QSqlQuery()
        q.prepare("SELECT distinct(max_jugadores) FROM juegos ORDER BY max_jugadores")
        listado = []
        if q.exec_():
            while q.next():
                listado.append(q.value(0))
        else:
            print("DB - Error al obtener listado de max jugadores: ", q.lastError().text())
        return listado

    def listadoGeneros(self):
        q = QtSql.QSqlQuery()
        q.prepare("SELECT distinct(genero) FROM juegos ORDER BY genero")
        listado = []
        if q.exec_():
            while q.next():
                listado.append(q.value(0))
        else:
            print("DB - Error al obtener listado de generos: ", q.lastError().text())
        return listado

    def listadoJuegosFiltrado(self, filtros):
        q = QtSql.QSqlQuery()
        consulta = self.consultaJuegos + " WHERE nombre LIKE :nombre"
        listado = []
        for i in filtros:
            if not i == "nombre":
                consulta = consulta + " AND " + i + " = '"+ str(filtros[i]) +"'"
        q.prepare(consulta)
        q.bindValue(":nombre", "%" + str(filtros["nombre"]) + "%")
        if q.exec_():
            listado = self.procesarConsultaJuegos(q)
        else:
            print("Error al cargar juegos filtrados: ", q.lastError().text())

        return listado

    def guardarJuego(self,juego):
        q = QtSql.QSqlQuery()

        if juego.id is None or juego.id == "": ## comprobamos que no exista.
            id = self.buscarIdComponente(juego)
            if id == -1: #si no existe, lo creamos
                q.prepare("INSERT INTO juegos (nombre, min_jugadores, max_jugadores, dificultad, genero, propietario, fecha_alta, descripcion, observaciones)  "
                    "VALUES ( :nombre, :minJugadores, :maxJugadores, :dificultad, :genero, :propietario, :fecha_alta, :descripcion, :observaciones)")
                q.bindValue(":fecha_alta", str(Herramientas.fechaActual()))
            else:
                juego.id = id # no lo creamos porque ya existe. lo actualizamos

        if juego.id is not None: #si el id no está vacio, es un update (no es un else, porque puede haber adquirido el id en las lineas anteriores.
            q.prepare("UPDATE juegos SET "
                      "nombre = :nombre,  min_jugadores = :minJugadores, max_jugadores = :maxJugadores, dificultad = :dificultad,"
                      "descripcion = :descripcion, observaciones = :observaciones, genero = :genero, propietario = :propietario "
                      "WHERE id = :id ")
            q.bindValue(":id", juego.id)

        q.bindValue(":nombre", juego.nombre)
        q.bindValue(":minJugadores", str(juego.minJugadores))
        q.bindValue(":maxJugadores", str(juego.maxJugadores))
        q.bindValue(":genero", str(juego.genero))
        q.bindValue(":descripcion", juego.descripcion)
        q.bindValue(":observaciones", juego.observaciones)

        if juego.dificultad is None:
            q.bindValue(":dificultad", "")
        else:
            q.bindValue(":dificultad", str(juego.dificultad.id))

        if juego.propietario is None:
            q.bindValue(":propietario", "")
        else:
            if juego.propietario.id is None: #si el propietario no existe. se busca o crea uno nuevo
               juego.propietario = self.guardarPropietario(juego.propietario)
            q.bindValue(":propietario", str(juego.propietario.id))

        if q.exec_():
            acciones.Acciones.anunciarStatusBar("Juego "+ juego.nombre+" guardado")
            return True
        else:
            acciones.Acciones.anunciarStatusBar("Error al guardar juego: ", q.lastError().text())
            return False

    def guardarListadoJuegos(self,listadoJuegos):
        for juego in listadoJuegos:
            self.guardarJuego(juego)
        acciones.Acciones.anunciarStatusBar("Listado de juegos guardado")

    def buscarIdComponente(self,componente):
        q = QtSql.QSqlQuery()
        if isinstance(componente,Juego):
            q.prepare("SELECT id FROM juegos WHERE nombre = :nombre ")
            q.bindValue(":nombre", componente.nombre)

        elif isinstance(componente, Propietario):
            q.prepare("SELECT id FROM propietarios WHERE nombre = :nombre ")
            q.bindValue(":nombre", componente.nombre)

        if q.exec_():
            if q.next():
                return q.value(0)
        return -1

    def guardarPropietario(self,propietario):
        if propietario.id is None:
            #compruebo si existe:
            q = QtSql.QSqlQuery()
            q.prepare("SELECT id FROM propietarios WHERE nombre = :nombre ")
            q.bindValue(":nombre", propietario.nombre)
            if q.exec_():
                if q.next():
                    print("El propietario: "+ propietario.nombre + " ya existe.")
                    propietario.id = q.value(0)
                else:
                    q = QtSql.QSqlQuery()
                    q.prepare(
                        "INSERT INTO propietarios (nombre)  "
                        "VALUES ( :nombre)")
                    q.bindValue(":nombre", propietario.nombre)
                    if q.exec_():
                        acciones.Acciones.anunciarStatusBar("Nuevo propietario "+ propietario.nombre+" guardado.")
                        propietario.id = q.lastInsertId()
                    else:
                        acciones.Acciones.anunciarStatusBar("Error al guardar propietario: ", q.lastError().text())
                return propietario
            else:
                print("Error al consultar propietario: ", q.lastError().text())


    def eliminarPropietario(self,propietario):
            if propietario.id is None:
                propietario.id = self.buscarIdComponente(propietario)

            if propietario.id != -1:
                q = QtSql.QSqlQuery()
                q.prepare(
                    "DELETE FROM propietarios WHERE id = :id")
                q.bindValue(":id", propietario.id)
                if q.exec_():
                    print("Propietario eliminado.")
                    q2 = QtSql.QSqlQuery()
                    q2.prepare("UPDATE juegos "
                                "SET propietario = '' "
                               "WHERE propietario = :id")
                    q2.bindValue(":id", propietario.id)
                    if q2.exec_():
                        acciones.Acciones.anunciarStatusBar("Propietario" + propietario.nombre+ " eliminado")
                    else:
                        acciones.Acciones.anunciarStatusBar("Error al eliminar propietarios de juegos : ", q.lastError().text())
                else:
                    acciones.Acciones.anunciarStatusBar("Error al eliminar propietario: ", q.lastError().text())
            else:
                acciones.Acciones.anunciarStatusBar("Error al eliminar propietario: El propietario no existe")
                #actualizamos juegos

    def eliminarJuego(self,juego):
            if juego.id is None:
                juego.id = self.buscarIdComponente(juego)
            if juego.id != -1:
                q = QtSql.QSqlQuery()
                q.prepare(
                    "DELETE FROM juegos WHERE id = :id")
                q.bindValue(":id", juego.id)
                if q.exec_():
                    acciones.Acciones.anunciarStatusBar("Juego " + juego.nombre + " eliminado")
                    return True
                else:
                    acciones.Acciones.anunciarStatusBar("Error al eliminar juego: ", q.lastError().text())
                    return False
            else:
                acciones.Acciones.anunciarStatusBar("Error al eliminar juego: no existe")
                #actualizamos juegos

