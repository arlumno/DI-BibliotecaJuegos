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
            print("Conexión realizada con éxito")
        return True

    def eliminarBD(self):
        self.disconnect()
        os.remove(self.fileDb);
        self.connect()
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

        if juego.id is None: ## comprobamos que no exista.
            id = self.buscarIdComponente(juego)
            if id == -1: #si no existe, lo creamos
                q.prepare("INSERT INTO juegos (nombre, min_jugadores, max_jugadores, dificultad, genero, propietario, fecha_alta, descripcion, observaciones)  "
                    "VALUES ( :nombre, :minJugadores, :maxJugadores, :dificultad, :genero, :propietario, :fecha_alta, :descripcion, :observaciones)")
                q.bindValue(":fecha_alta", str(Herramientas.fechaActual()))
            else:
                juego.id = id # no lo creamos porque ya existe. lo actualizamos

        if juego.id is not None: ##si el id no está vacio, es un update
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

            print("Juego guardado")
            return True
        else:
            print("Error al guardar juego: ", q.lastError().text())
            return False

    def guardarListadoJuegos(self,listadoJuegos):
        for juego in listadoJuegos:
            self.guardarJuego(juego)

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
                        print("Nuevo propietario guardado.")
                        propietario.id = q.lastInsertId()
                    else:
                        print("Error al guardar propietario: ", q.lastError().text())
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
                        print(" eliminado propietarios de juego")
                    else:
                        print("Error al eliminar propietarios de juegos : ", q.lastError().text())
                else:
                    print("Error al eliminar propietario: ", q.lastError().text())
            else:
                print("El propietario no existe")
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
                    return True
                else:
                    print("Error al eliminar juego: ", q.lastError().text())
                    return False
            else:
                print("El Juego no existe")
                #actualizamos juegos


# ******************************************************************************************************************************************************


#     def modificarCliente(cliente):
#         q = QtSql.QSqlQuery()
#         print(cliente)
#         q.prepare(
#             "UPDATE clientes "
#             "SET apellidos = :apellidos,  nombre = :nombre, direccion = :direccion, provincia = :provincia, fecha_alta = :fecha_alta, forma_pago = :pago, sexo = :sexo, envio = :envio "
#             "WHERE dni = :dni ")
#
#         q.bindValue(":dni", str(cliente[0]))
#         q.bindValue(":apellidos", str(cliente[1]))
#         q.bindValue(":nombre", str(cliente[2]))
#         q.bindValue(":direccion", str(cliente[3]))
#         q.bindValue(":fecha_alta", str(cliente[4]))
#         q.bindValue(":provincia", str(cliente[5]))
#         q.bindValue(":pago", str(cliente[6]))
#         q.bindValue(":sexo", str(cliente[7]))
#         q.bindValue(":envio", str(cliente[8]))
#
#         if q.exec_():
#             return True
#         else:
#             print("Error al modificar cliente: ", q.lastError().text())
#             return False
#

#     def eliminarCliente(dni):
#         q = QtSql.QSqlQuery()
#         if Acciones.Acciones.isClientecargado():
#             Database.obtenerCliente(dni)
#             q.prepare(
#                 "DELETE FROM clientes "
#                 "WHERE dni = :dni ")
#             q.bindValue(":dni", dni)
#
#             if q.exec_():
#                 return True
#             else:
#                 return False
#                 print("Error al eliminar cliente: ", q.lastError().text())
#         else:
#             Tools.ventanaAdvertencia("El cliente que se intenta borrar no Existe")
#
#     def cargarClientes():
#         q = QtSql.QSqlQuery()
#         q.prepare(
#             "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio FROM clientes")
#         var.listadoClientes = []
#         if q.exec_():
#             while q.next():
#                 var.listadoClientes.append(
#                     [q.value(0), q.value(1), q.value(2), q.value(3), q.value(5), q.value(6), q.value(7), q.value(4),
#                      q.value(8)])
#
#         else:
#             print("Error al cargar clientes: ", q.lastError().text())
#
#     def cargarProvincias():
#         q = QtSql.QSqlQuery()
#         q.prepare("SELECT provincia FROM provincias")
#         var.listadoProvincias = [""]
#         if q.exec_():
#             while q.next():
#                 var.listadoProvincias.append(q.value(0))
#         else:
#             print("Error al cargar provincias: ", q.lastError().text())
#
#     def importarListadoClientes(listadoClientesImportar):
#         clientesNuevos = 0
#         clientesActualizados = 0
#         for cliente in listadoClientesImportar:
#             if Database.obtenerCliente(cliente[0]) is None:
#                 if cliente[4] == "":
#                     cliente[4] = Tools.fechaActual()
#                 Database.guardarCliente(cliente)
#                 clientesNuevos += 1
#             else:
#                 Database.modificarCliente(cliente)
#                 clientesActualizados += 1
#
#         Tools.ventanaAdvertencia(
#             "Importación completada.\n Clientes nuevos: " + str(clientesNuevos) + "\n clientes actualizados: " + str(
#                 clientesActualizados))
#
#         Acciones.Acciones.anunciarStatusBar("Importados " + str(len(listadoClientesImportar)) + " clientes")
#
#     def filtrarClientes(filtro):
#         q = QtSql.QSqlQuery()
#
#         # q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes WHERE nombre = :filtro")
#         q.prepare(
#             "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio FROM clientes WHERE nombre LIKE :filtro or apellidos LIKE :filtro")
#
#         q.bindValue(":filtro", "%" + str(filtro) + "%")
#
#         var.listadoClientes = []
#         if q.exec_():
#             while q.next():
#                 var.listadoClientes.append(
#                     [q.value(0), q.value(1), q.value(2), q.value(3), q.value(5), q.value(6), q.value(7), q.value(4),
#                      q.value(8)])
#         else:
#             print("Error al cargar clientes: ", q.lastError().text())
#
#     def borrarClientes():
#         q = QtSql.QSqlQuery()
#         q.prepare('DELETE FROM clientes')
#         if q.exec_():
#             return True
#         else:
#             print("Error al cargar clientes: ", q.lastError().text())
#             return False
#
#     def obtenerListadoClientes():
#         q = QtSql.QSqlQuery()
#         q.prepare(
#             "SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo, envio, codigo FROM clientes")
#         listado = []
#         if q.exec_():
#             while q.next():
#                 listado.append(
#                     {"dni": q.value(0),
#                      "apellidos": q.value(1),
#                      "nombre": q.value(2),
#                      "direccion": q.value(3),
#                      "fecha_alta": q.value(4),
#                      "provincia": q.value(5),
#                      "forma_pago": q.value(6),
#                      "sexo": q.value(7),
#                      "envio": q.value(8),
#                      "codigo": q.value(9)
#                      }
#                 )
#         else:
#             print("Error al obtener lista de  clientes: ", q.lastError().text())
#         # print(listado)
#         return listado
