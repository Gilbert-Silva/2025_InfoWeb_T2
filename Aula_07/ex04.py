class Agua:
    def __init__(self):
        self.mes = 1
        self.ano = 2025
        self.consumo = 0
    def valor(self):
        if self.consumo <= 10: return 38
        if 11 <= self.consumo <= 20: return 38 + (self.consumo - 10) * 5
        if self.consumo > 20: return 38 + 50 + (self.consumo - 20) * 6  

x = Agua()
x.mes = int(input("Informe o mês da conta: "))
x.ano = int(input("informe o ano: "))
x.consumo = int(input("informe o consumo em m3: "))
print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é {x.valor()}")