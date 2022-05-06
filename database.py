import os.path
import shutil
import sys
import tempfile

from PyQt5 import QtWidgets, QtSql

import var
import acciones
from ClasesComponentes import *
import constructor
from Herramientas import Herramientas


class Database():
    fileDb = "app.db"
    fileDbEmpty = "app.empty.db"
    consultaJuegos = "SELECT id, nombre, min_jugadores, max_jugadores, dificultad, genero, propietario, fecha_alta FROM juegos"

    def __init__(self):
        self.db = None

    def connect(self):
        if not os.path.isfile(self.fileDb):
            Herramientas.ventanaAdvertencia("No hay ninguna base de datos creada. \n Se procede a crear una nueva.","No Database")
            shutil.copy(sys._MEIPASS+'/'+self.fileDbEmpty, self.fileDb)

        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.fileDb)
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, "No se puede abrir la base de datos",
                                           'No se puede establecer conexión.', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print("Conexión realizada con éxito")
        return True

    def disconnect(self):
        self.db.close()
        print("Base de datos desconectada.")

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

        if juego.id is None: ## es un insert.
            q.prepare(
                "INSERT INTO juegos (nombre, min_jugadores, max_jugadores, dificultad, genero, propietario, fecha_alta)  "
                "VALUES ( :nombre, :minJugadores, :maxJugadores, :dificultad, :genero, :propietario, :fecha_alta)")

            q.bindValue(":nombre", juego.nombre)
            q.bindValue(":minJugadores", str(juego.minJugadores))
            q.bindValue(":maxJugadores", str(juego.maxJugadores))

            if juego.dificultad is None:
                q.bindValue(":dificultad", "")
            else:
                q.bindValue(":dificultad", str(juego.dificultad.id))

            if juego.propietario is None:
                q.bindValue(":propietario", "")
            # elif juego.propietario.id is None: #si el propietario no existe. se busca o crea uno nuevo
            #     if juego.propietario.nombre in var.propietariosByNombre:
            #         juego.
            else:
                q.bindValue(":propietario", str(juego.propietario.id))
                q.bindValue(":propietario", str(juego.propietario.id))

            q.bindValue(":genero", str(juego.genero))

            q.bindValue(":fecha_alta", str(Herramientas.fechaActual()))

            print("Juego guardado")
        else: ##es un update
            #TODO
            print("juego actualizado")
        if q.exec_():
            return True
        else:
            print("Error al guardar cliente: ", q.lastError().text())
            return False

#    def guardarListadoJuegos(listadoJuegos):

    def guardarPropietario(propietario):
        if propietario.id is None:

        else: #TODO actualiza




# ******************************************************************************************************************************************************

    def guardarCliente(cliente):
        q = QtSql.QSqlQuery()

        q.prepare(
            "INSERT INTO clientes (dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio)  "
            "VALUES ( :dni, :apellidos, :nombre, :direccion, :fecha_alta, :provincia, :pago, :sexo, :envio)")

        q.bindValue(":dni", str(cliente[0]))
        q.bindValue(":apellidos", str(cliente[1]))
        q.bindValue(":nombre", str(cliente[2]))
        q.bindValue(":direccion", str(cliente[3]))
        q.bindValue(":fecha_alta", str(cliente[4]))
        q.bindValue(":provincia", str(cliente[5]))
        q.bindValue(":pago", str(cliente[6]))
        q.bindValue(":sexo", str(cliente[7]))
        q.bindValue(":envio", str(cliente[8]))

        if q.exec_():
            return True
        else:
            print("Error al guardar cliente: ", q.lastError().text())
            return False

    def modificarCliente(cliente):
        q = QtSql.QSqlQuery()
        print(cliente)
        q.prepare(
            "UPDATE clientes "
            "SET apellidos = :apellidos,  nombre = :nombre, direccion = :direccion, provincia = :provincia, fecha_alta = :fecha_alta, forma_pago = :pago, sexo = :sexo, envio = :envio "
            "WHERE dni = :dni ")

        q.bindValue(":dni", str(cliente[0]))
        q.bindValue(":apellidos", str(cliente[1]))
        q.bindValue(":nombre", str(cliente[2]))
        q.bindValue(":direccion", str(cliente[3]))
        q.bindValue(":fecha_alta", str(cliente[4]))
        q.bindValue(":provincia", str(cliente[5]))
        q.bindValue(":pago", str(cliente[6]))
        q.bindValue(":sexo", str(cliente[7]))
        q.bindValue(":envio", str(cliente[8]))

        if q.exec_():
            return True
        else:
            print("Error al modificar cliente: ", q.lastError().text())
            return False

    def obtenerCliente(dni):
        q = QtSql.QSqlQuery()
        q.prepare(
            "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio FROM clientes WHERE dni = :dni")
        q.bindValue(":dni", str(dni))

        if q.exec_():
            q.next()
            cliente = [q.value(0), q.value(1), q.value(2), q.value(3), q.value(5), q.value(6), q.value(7), q.value(4),
                       q.value(8)]
            # Acciones.Acciones.obtenerCliente(cliente)
            if cliente[0] is None:
                cliente = None
        else:
            cliente = None
            print("Error al cargar el cliente: ", q.lastError().text())
        return cliente

    def eliminarCliente(dni):
        q = QtSql.QSqlQuery()
        if Acciones.Acciones.isClientecargado():
            Database.obtenerCliente(dni)
            q.prepare(
                "DELETE FROM clientes "
                "WHERE dni = :dni ")
            q.bindValue(":dni", dni)

            if q.exec_():
                return True
            else:
                return False
                print("Error al eliminar cliente: ", q.lastError().text())
        else:
            Tools.ventanaAdvertencia("El cliente que se intenta borrar no Existe")

    def cargarClientes():
        q = QtSql.QSqlQuery()
        q.prepare(
            "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio FROM clientes")
        var.listadoClientes = []
        if q.exec_():
            while q.next():
                var.listadoClientes.append(
                    [q.value(0), q.value(1), q.value(2), q.value(3), q.value(5), q.value(6), q.value(7), q.value(4),
                     q.value(8)])

        else:
            print("Error al cargar clientes: ", q.lastError().text())

    def cargarProvincias():
        q = QtSql.QSqlQuery()
        q.prepare("SELECT provincia FROM provincias")
        var.listadoProvincias = [""]
        if q.exec_():
            while q.next():
                var.listadoProvincias.append(q.value(0))
        else:
            print("Error al cargar provincias: ", q.lastError().text())

    def importarListadoClientes(listadoClientesImportar):
        clientesNuevos = 0
        clientesActualizados = 0
        for cliente in listadoClientesImportar:
            if Database.obtenerCliente(cliente[0]) is None:
                if cliente[4] == "":
                    cliente[4] = Tools.fechaActual()
                Database.guardarCliente(cliente)
                clientesNuevos += 1
            else:
                Database.modificarCliente(cliente)
                clientesActualizados += 1

        Tools.ventanaAdvertencia(
            "Importación completada.\n Clientes nuevos: " + str(clientesNuevos) + "\n clientes actualizados: " + str(
                clientesActualizados))

        Acciones.Acciones.anunciarStatusBar("Importados " + str(len(listadoClientesImportar)) + " clientes")

    def filtrarClientes(filtro):
        q = QtSql.QSqlQuery()

        # q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes WHERE nombre = :filtro")
        q.prepare(
            "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio FROM clientes WHERE nombre LIKE :filtro or apellidos LIKE :filtro")

        q.bindValue(":filtro", "%" + str(filtro) + "%")

        var.listadoClientes = []
        if q.exec_():
            while q.next():
                var.listadoClientes.append(
                    [q.value(0), q.value(1), q.value(2), q.value(3), q.value(5), q.value(6), q.value(7), q.value(4),
                     q.value(8)])
        else:
            print("Error al cargar clientes: ", q.lastError().text())

    def borrarClientes():
        q = QtSql.QSqlQuery()
        q.prepare('DELETE FROM clientes')
        if q.exec_():
            return True
        else:
            print("Error al cargar clientes: ", q.lastError().text())
            return False

    def obtenerListadoClientes():
        q = QtSql.QSqlQuery()
        q.prepare(
            "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio, codigo FROM clientes")
        listado = []
        if q.exec_():
            while q.next():
                listado.append(
                    {"dni": q.value(0),
                     "apellidos": q.value(1),
                     "nombre": q.value(2),
                     "direccion": q.value(3),
                     "fecha_alta": q.value(4),
                     "provincia": q.value(5),
                     "forma_pago": q.value(6),
                     "sexo": q.value(7),
                     "envio": q.value(8),
                     "codigo": q.value(9)
                     }
                )
        else:
            print("Error al obtener lista de  clientes: ", q.lastError().text())
        # print(listado)
        return listado
