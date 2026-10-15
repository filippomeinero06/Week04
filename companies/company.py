from employee import Employee
from manager import Manager
from car import Car

e1 = Employee("Mr. Bean", 15000)

print(e1)

m = Manager("B. Boss", 40000, "HR")

print(m)

print("-----Incremento della paga:-----")
e1.increment_wage()
print(e1)

m.increment_wage()
print(m)


print("******* Struttura dati *******")
users = []
users.append(e1)
users.append(m)

# DUCK TIPING: si possono mettere nella struttura dati anche altri tipi di "oggetti" ma se hanno le funzioni che andiamo a chiamare (la stampa) allora si possono mettere all'interno
users.append("abcdefg")
users.append(2)

c1 = Car("AB123CD", "Red", "False")
users.append(c1) # se si stampa printa l'indirizzo di memoria perché nella classe Car non abbiamo definito __str()__, ora lo facciamo

for user in users:
    print(f"{user} | {type(user)}")

# Esempio, se in Car il metodo __str__() non è definito, quando stampato verrà mostrato nella console di riferimento

if isinstance(e1, Employee):
    print("e1 è un Employee")
else:
    print("e1 non è un employee")