from persona import Persona
# Per dire che la classe Docente EREDITA da Persona devo inserire il nome della classe tra ()

class Docente(Persona):
    def __init__(self, nome, cognome, dipartimento):
        # SBAGLIATO RIPETERE LA DEFINIZIONE DEGLI ATTR. DEL PADRE
        # self.__nome = nome
        # self.__cognome = cognome

        super().__init__(nome, cognome) # Costruisce "la parte" Persona del Docente (prima costruisco la parte Persona e poi aggiungo gli attributi specifici per Docente)
        self.dipartimento = dipartimento
