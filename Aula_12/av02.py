class Energia:
    def __init__(self, mes, ano, consumo):  # atributos - 10
        self.__mes = 1                      # validação - 10
        self.__ano = 2025                   # encapsulamento - 10
        self.__consumo = 100                # get - 10
        self.set_mes(mes)                   # set - 10
        self.set_ano(ano)                   # cálculo - 10
        self.set_consumo(consumo)

    def set_mes(self, mes):
        if mes < 1 or mes > 12: raise ValueError()
        self.__mes = mes
    def set_ano(self, ano):
        if ano < 2020: raise ValueError()
        self.__ano = ano
    def set_consumo(self, consumo):
        if consumo < 0: raise ValueError()
        self.__consumo = consumo

    def get_mes(self): 
        return self.__mes
    def get_ano(self): 
        return self.__ano
    def get_consumo(self): 
        return self.__consumo

    def valor(self):
        if self.__consumo <= 300: return self.__consumo * 0.9
        return self.__consumo * 1.05

    def __str__(self):
        return f"{self.__mes}/{self.__ano}, {self.__consumo}"

class EnergiaUI:                              # main - 5
    @staticmethod                                # menu - 5
    def main():                                  # input - 5 
        op = 0                                   # instância - 5
        while op != 2:                           # print - 5
            op = EnergiaUI.menu()             # cálculo - 5
            if op == 1: EnergiaUI.calculo()   # sintaxe - 10

    @staticmethod
    def menu():
        print("Escolha uma opção")
        return int(input("1 - Energia, 2 - Fim: "))
    
    @staticmethod
    def calculo():
        mes = int(input("Informe o mês: "))
        ano = int(input("Informe o ano: "))
        consumo = int(input("Informe o consumo: "))
        x = Energia(mes, ano, consumo)
        print(x)
        print(x.valor())

EnergiaUI.main()      


