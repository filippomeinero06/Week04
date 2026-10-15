from companies.employee import Employee

class Manager(Employee):

    def __init__(self, name, wage, managedUnit):
        # Prima istruzione del costruttore di una classe figlia è l'invocazione della costruzione del padre
        # in virtù dell'approccio "a cipolla"
        super().__init__(name, wage)
        self.__managedUnit = managedUnit

    # Con la OOP posso andare a ridefinire i metodi che non mi piacciono del padre andando a specificare
    # comportamenti specializzati nel figlio
    def __str__(self):
        return f"{super().__str__()} {self.__managedUnit}"

    # Se non vogliamo usare il metodo della classe padre nel figlio, lo possiamo ridefinire

    # I metodi ridefiniti nei figli con lo stesso nome si dicono OVERRIDING
    def increment_wage(self):
        self.wage += 10000

