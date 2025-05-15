class Agua:
    def __init__(self):
        self.mes = 1
        self.ano = 2025
        self.consumo = 0
    def valor(self):
        if self.consumo <= 10: return 38
        if 11 <= self.consumo <= 20: return 38 + (self.consumo - 10) * 5
        if self.consumo > 20: return 38 + 50 + (self.consumo - 20) * 6  

class Triangulo():
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2  

class UI: # UI = User Interface: print e input
    @staticmethod
    def menu():
        op = int(input("Informe uma opção: 1-Conta d'água, 2-Triângulo, 9-Fim: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
           # op = self.menu()
           op = UI.menu()
           if op == 1: UI.agua()
           if op == 2: UI.triangulo()
    @staticmethod
    def agua():
        x = Agua() # x é um objeto da classe Água
        x.mes = int(input("Informe o mês da conta: "))
        x.ano = int(input("informe o ano: "))
        x.consumo = int(input("informe o consumo em m3: "))
        print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é {x.valor()}")
    @staticmethod
    def triangulo():
        x = Triangulo() # x é um objeto da classe Triangulo
        x.b = int(input("Informe o valor da base: "))
        x.h = int(input("Informe o valor da altura: "))
        print(f"O triângulo de base {x.b} e altura {x.h} tem área {x.calc_area()}")

#x = UI()
#x.main()
UI.main()

