import os.path
import shutil
import sys
import tempfile

from PyQt5 import QtWidgets, QtSql

import var
import Acciones
from Juego import Juego
from Herramientas import Herramientas


class Database():
    fileDb = "app.db"
    fileDbEmpty = "app.empty.db"

    def __init__(self):
        self.db = None

    def connect(self):
        if not os.path.isfile(self.fileDb):
            tools.Tools.ventanaAdvertencia("No hay ninguna base de datos creada. \n Se procede a crear una nueva.","No Database")
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
        q.prepare( "SELECT id, nombre, min_jugadores, max_jugadores FROM juegos")
        listado = []
        if q.exec_():
            while q.next():
                juego = Juego(q.value(0), q.value(1),q.value(2),q.value(3) )
                listado.append(juego)
        else:
            print("Error al obtener listatado de juegos: ", q.lastError().text())
        return listado
















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
