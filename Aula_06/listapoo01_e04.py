class Ingresso:
    def __init__(self):
        self.dia = "dom"
        self.hora = 18
    def entrada_inteira(self):
        if self.dia == "qua" : return 8
        valor = 16
        if self.dia == "sex" or self.dia == "sab" or self.dia == "dom":
            valor = 20
        if self.hora == 0 or self.hora >= 17: valor = 1.5 * valor
        return valor
    def meia_entrada(self):
        if self.dia == "qua" : return 8
        return self.entrada_inteira() / 2
    
x = Ingresso()
print(x.dia, x.hora)
print(x.entrada_inteira())  # self é x
print(x.meia_entrada())

y = Ingresso()
y.dia = "seg"
y.hora = 15
print(y.dia, y.hora)
print(y.entrada_inteira())  # self é y
print(y.meia_entrada())

z = Ingresso()
z.dia = "qua"
z.hora = 20
print(z.dia, z.hora)
print(z.entrada_inteira())  # self é z
print(z.meia_entrada())


