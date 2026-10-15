class Persona:
    # numero_teste = 1 # Variabile di classe

    def __init__(self, nome, cognome):
        self.__nome = nome # Attributi / Variabili di istanza
        self.__cognome = cognome

    @property
    def nome(self):
        return self.__nome

    def mangia(self):
        pass

    def beve(self):
        pass

    def __str__(self):
        return f"{self.__nome} {self.__cognome}"

# p1 = Persona("Mario", "Rossi")
# p2 = Persona("Luigi", "Neri")

# Persona.numero_teste = 3 # Servono per trasportare informazioni comuni a tutte le istanze della classe
# print(p1.numero_teste)

# p1.codice_fiscale = "LMBFRZ75B..." # Questa variabile viene aggiunta solo nell'istanza p1, ma non viene aggiunta a tutte le istanze

