class Conta:
    def __init__(self):
        self.__titular = ""
        self.__numero = ""
        self.__saldo = 0.0

    def set_titular(self, t):
        if t == "": raise ValueError("Nome não pode ser vazio")
        self.__titular = t

    def get_titular(self):
        return self.__titular

    def set_numero(self, n):
        if n == "": raise ValueError("Número da conta não pode ser vazio")
        self.__numero = n

    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo

    def depositar(self, v):
        if v < 0: raise ValueError("Valor não pode ser negativo")
        self.__saldo += v

    def sacar(self, v):
        if v < 0: raise ValueError("Valor não pode ser negativo")
        if v > self.__saldo: raise ValueError("Saldo insuficiente")
        self.__saldo -= v

class UI:
    def menu():
        print("1-Abrir conta, 2-Mostrar dados, 3-Saldo, 4-Depositar, 5-Sacar, 9-Fim")
        return int(input("Informe uma opção: "))
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            match op:
                case 1: x = UI.abrir_conta()
                case 2: UI.mostrar_dados(x)
                case 3: UI.mostrar_saldo(x)
                case 4: UI.depositar(x)
                case 5: UI.sacar(x)
    def abrir_conta():
        x = Conta()
        x.set_titular(input("Informe seu nome: "))
        x.set_numero(input("Informe o número da conta: "))
        return x
    def mostrar_dados(x):
        print("Dados da conta")
        print("Titular:", x.get_titular())
        print("Número", x.get_numero())
    def mostrar_saldo(x):
        print("Seu saldo:", x.get_saldo())
    def depositar(x):
        x.depositar(float(input("Informe o valor do depósito: ")))
    def sacar(x):
        x.sacar(float(input("Informe o valor do saque: ")))

UI.main()        

                            
                        



        
