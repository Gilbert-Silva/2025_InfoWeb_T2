from datetime import datetime
from enum import Enum

class Dias(Enum):
    Segunda = 0
    Terça = 1
    Quarta = 2
    Quinta = 3
    Sexta = 4
    Sábado = 5
    Domingo = 6

dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

x = datetime(2025, 6, 4)   # init de datetime
print(x)
print(type(x))
hoje = datetime.now()         # now é método de classe
print(hoje)
print(hoje.strftime("%d/%m/%Y"))  # método de instância
print(dias[hoje.weekday()])
print(Dias(hoje.weekday()))

d = input("Informe sua data de nascimento: ")
dn = datetime.strptime(d, "%d/%m/%Y")
print(d, type(d))
print(dn, type(dn))

print(dias[dn.weekday()])


dv = hoje - dn
print(dv)
print(type(dv))

print(dv.days // 365, "anos")
print(dv.days % 365 // 30, "meses")
print(dv.days % 365 % 30, "dias")


