from operator import attrgetter

class LaMiaClasse():
    def __init__(self, attributo):
        self.attributo = attributo

    def __str__(self):
        return f"{self.attributo}"

    def __repr__(self):
        return f"{type(self)} {self.attributo}"

    # Posso ridefinire il metodo __eq__() che è il metodo di confronto (in overriding), andando a scrivere
    # al suo interno l'algoritmo di confronto
    def __eq__(self, other):
        if self.attributo == other.attributo:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.attributo < other.attributo:
            return True
        else:
            return False

o1 = LaMiaClasse("Pippo")

print(o1) # __str__()

o2 = LaMiaClasse("Pluto")

# Come faccio a confrontare due oggetti o1 e o2

if o1 == o2:    # o1.__eq__(o2)
    print("Uguali")
else:
    print("Diversi")

print(o1.__repr__())

print("-----------------------")

lista = [o1]
lista.append(o2)
lista.append(LaMiaClasse("Gastone"))

lista.sort(key=attrgetter("attributo"))

for e in lista:
    print(e)