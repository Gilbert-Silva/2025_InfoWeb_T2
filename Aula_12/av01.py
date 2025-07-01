class Disciplina:
    def __init__(self, nome, n1, n2, nf):   # atributos - 10
        self.__nome = ""                    # validação - 10
        self.__n1 = 0                       # encapsulamento - 10
        self.__n2 = 0                       # get - 10
        self.__nf = 0                       # set - 10
        self.set_nome(nome)                 # cálculo - 10
        self.set_n1(n1)
        self.set_n2(n2)
        self.set_nf(nf)

    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_n1(self, n1):
        if n1 < 0 or n1 > 100: raise ValueError()
        self.__n1 = n1
    def set_n2(self, n2):
        if n2 < 0 or n2 > 100: raise ValueError()
        self.__n2 = n2
    def set_nf(self, nf):
        if nf < 0 or nf > 100: raise ValueError()
        self.__nf = nf

    def get_nome(self): 
        return self.__nome
    def get_n1(self): 
        return self.__n1
    def get_n2(self): 
        return self.__n2
    def get_nf(self): 
        return self.__nf

    def media(self):
        mp = (2 * self.__n1 + 3 * self.__n2) / 5
        if mp >= 60: return mp
        return (1 * mp + 1 * self.__nf) / 2

    def __str__(self):
        return f"{self.__nome}: {self.__n1}, {self.__n2}, {self.__nf}"

class DisciplinaUI:                              # main - 5
    @staticmethod                                # menu - 5
    def main():                                  # input - 5 
        op = 0                                   # instância - 5
        while op != 2:                           # print - 5
            op = DisciplinaUI.menu()             # cálculo - 5
            if op == 1: DisciplinaUI.calculo()   # sintaxe - 10

    @staticmethod
    def menu():
        print("Escolha uma opção")
        return int(input("1 - Disciplina, 2 - Fim: "))
    
    @staticmethod
    def calculo():
        nome = input("Informe o nome da disciplina: ")
        n1 = int(input("Informe a 1ª nota: "))
        n2 = int(input("Informe a 2ª nota: "))
        nf = int(input("Informe a nota da prova final: "))
        x = Disciplina(nome, n1, n2, nf)
        print(x)
        print(x.media())

DisciplinaUI.main()      


