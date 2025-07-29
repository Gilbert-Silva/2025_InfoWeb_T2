from views import View

class UI:
    @staticmethod    
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()

    @staticmethod    
    def menu():
        print("1-Inserir, 2-Listar, 3-Fim")
        return int(input("Informe sua opção: "))
    
    @staticmethod    
    def inserir():
        nome = input("Informe o nome do cliente: ")
        View.cliente_inserir(nome)
        print("Cliente inserido com sucesso")

    @staticmethod    
    def listar():
        for cliente in View.cliente_listar():
            print(cliente)

UI.main()
