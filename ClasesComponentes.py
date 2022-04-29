class Juego():
    def __init__(self, id, nombre, min_jugadores, max_jugadores):
        self.id = id
        self.nombre = nombre
        self.minJugadores = min_jugadores
        self.maxJugadores = max_jugadores
        self.dificultad = ""
        self.genero = ""
        self.propietario = ""
        self.fechaAlta = ""
        self.descripcion = ""
        self.observaciones = ""

    def __str__(self):
        text = str(self.id) + " - " \
               + str(self.nombre) + " - " \
               + str(self.minJugadores) + " - " \
               + str(self.maxJugadores) + " - " \
               + str(self.dificultad) + " - " \
               + str(self.genero) + " - " \
               + str(self.propietario) + " - " \
               + str(self.fechaAlta) + " - " \
               + str(self.descripcion) + "\n\t - " \
               + str(self.observaciones) + "\n\t - "
        return text


class Propietario():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        text = str(self.id) + " - " \
               + str(self.nombre) + " - "
        return text


class Dificultad():
    def __init__(self, id, dificultad):
        self.id = id
        self.dificultad = dificultad

    def __str__(self):
        text = str(self.id) + " - " \
               + str(self.dificultad) + " - "
        return text
