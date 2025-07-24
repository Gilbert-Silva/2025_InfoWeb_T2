from datetime import datetime, timedelta

# Atributos - 6
# Encapsulamento - 6
# Validação - 6
# Init - 6
# Get - 6
# Set - 6
# Chegada - 8
# Str - 6


class Voo:
    def __init__(self, codigo, partida, duracao):
        self.set_codigo(codigo)
        self.set_partida(partida)
        self.set_duracao(duracao)
    def set_codigo(self, codigo):
        if codigo == "": raise ValueError("Não pode ser vazio")
        self.__codigo = codigo    
    def set_partida(self, partida):
        if partida < datetime.now(): raise ValueError("Não pode no passado")
        self.__partida = partida        
    def set_duracao(self, duracao):
        if duracao < timedelta(0): raise ValueError("Não pode ser tempo negativo")
        self.__duracao = duracao   
    def get_codigo(self): return self.__codigo
    def get_partida(self): return self.__partida
    def get_duracao(self): return self.__duracao
    def chegada(self): return self.__partida + self.__duracao # datetime + timedelta -> datetime
    def __str__(self):
        return f"{self.__codigo} {self.__partida} {self.__duracao}"
    
# Atributo - 5
# Main - 5
# Menu - 5
# Inserir - input - 5
# Inserir - conversão - 5
# Inserir - init - 5
# Inserir - append - 5
# Listar - 5
# Calcular - 10

class UI:
    __objetos = []
    @classmethod
    def main(cls):
        op = 0
        while op != 4:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.calcular()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Calcular, 4-Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        codigo = input("Informe o código do Voo: ")
        partida = datetime.strptime(input("Informe data e horário do voo: "), "%d/%m/%Y %H:%M")
        horas, minutos = map(int, input("Informe a duração hh:mm: ").split(":"))
        duracao = timedelta(hours=horas, minutes=minutos)
        voo = Voo(codigo, partida, duracao)
        cls.__objetos.append(voo)

    @classmethod
    def listar(cls):
        for voo in cls.__objetos: print(voo)

    @classmethod
    def calcular(cls):
        m = cls.__objetos[0]
        for voo in cls.__objetos:
            if voo.get_duracao() > m.get_duracao(): m = voo
        print(m)    

UI.main()
