from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

from database import Database
from Herramientas import Herramientas
import var


class Informes():

    def configReport():
        var.configReport = {"rutaArchivoPdf":'listado_juegos.pdf',
                            "tituloInforme": "Listado de Juegos",
                            "autorInforme": "Armando Castro",
                            "logoEmpresa": "recursos/logo_dados.png",
                            "nombreEmpresa": "Asociacion Viguesa de juegos de mesa.",
                            "direccionEmpresa": "Avenida Galicia, 9999 - 36216 Vigo (Pontevedra)",
                            "telefonoEmpresa": "897 12 04 64"
                            }

    def reportCli():
        try:
            Informes.configReport()
            var.report = canvas.Canvas(var.configReport['rutaArchivoPdf'], pagesize=A4)
            Informes.header()

            var.report.setFont('Helvetica-Bold', size=13)
            var.report.drawString(55,730, var.configReport['tituloInforme'])

            listadoJuegos = var.db.listadoJuegos();

            Informes.body(listadoJuegos)

            Informes.footer()

            var.report.save()
            os.startfile(".\\"+var.configReport['rutaArchivoPdf'])
        except Exception as error:
            print('Error reporcli %s ' % str(error))

    def header():
        try:
            var.report.setTitle(var.configReport['tituloInforme'])
            var.report.setAuthor(var.configReport['autorInforme'])
            var.report.setFont('Helvetica', size=10)
            var.report.line(45,820,525,820)
            var.report.line(45,745,525,745)

            var.report.drawString(50,790,var.configReport['nombreEmpresa'])
            var.report.drawString(50,775,var.configReport['direccionEmpresa'])
            var.report.drawString(50,760,var.configReport['telefonoEmpresa'])
            var.report.drawImage(var.configReport['logoEmpresa'], 455, 752,60,60)
            Informes.subHeader()

        except Exception as error:
            print('Error reporcli header %s ' % str(error))

    def subHeader():
        var.report.line(45, 722, 525, 722)
        var.report.setFont("Helvetica", size=9)
        var.report.drawString(45, 710, 'Cod.')
        var.report.drawString(80, 710, 'Nombre')
        var.report.drawString(185, 710, "Jugadores")
        var.report.drawString(245, 710, "Genero")
        var.report.drawString(340, 710, "Dificultad")
        var.report.drawString(405, 710, "Propietario")
        var.report.drawString(475, 710, "Fecha Alta")
        var.report.line(45, 703, 525, 703)
    def body(listadoJuegos):
        try:
            i = 675
            j = i
            for juego in listadoJuegos:
                var.report.setFont('Helvetica', size=8)
                var.report.drawString(50, j, str(juego.id))
                var.report.drawString(70, j, juego.nombre)
                var.report.drawString(195, j, (str(juego.minJugadores) + " - " + str(juego.maxJugadores)))
                var.report.drawString(240, j, juego.genero)
                if juego.dificultad is None:
                    dificultad = ""
                else:
                    dificultad = juego.dificultad.dificultad
                var.report.drawString(345, j, dificultad)
                if juego.propietario is None:
                    propietario = ""
                else:
                    propietario = juego.propietario.nombre
                var.report.drawString(410, j, propietario)
                var.report.drawRightString(525, j, str(juego.fechaAlta))
                j = j - 30
                if j < 70:
                    Informes.footer()
                    var.report.showPage()
                    Informes.header()
                    j = i
        except Exception as error:
            print('Error reporcli body %s ' % str(error))

    def footer():
        try:
            var.report.setFont("Helvetica", size=7)
            var.report.line(50,50,525,50)
            fecha = Herramientas.fechaActual('%d.%m.%Y %H.%M.%S')
            var.report.drawString(460,40, fecha)
            var.report.drawString(275,40, str('Página %s' % var.report.getPageNumber()))
            var.report.drawString(50,40, var.configReport['tituloInforme'] + "  Autor: " + var.configReport['autorInforme'])

        except Exception as error:
            print('Error reporcli footer %s ' % str(error))