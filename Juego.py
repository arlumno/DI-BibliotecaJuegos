class Juego():
    def __init__(self,id, nombre,min_jugadores,max_jugadores ):
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