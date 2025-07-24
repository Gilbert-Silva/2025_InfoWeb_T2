from datetime import datetime, timedelta
import json

# Atributos - 6
# Encapsulamento - 6
# Validação - 6
# Init - 6
# Get - 6
# Set - 6
# Chegada - 8
# Str - 6


class Cinema:
    def __init__(self, filme, inicio, duracao):
        self.set_filme(filme)
        self.set_inicio(inicio)
        self.set_duracao(duracao)
    def set_filme(self, filme):
        if filme == "": raise ValueError("Não pode ser vazio")
        self.__filme = filme    
    def set_inicio(self, inicio):
        if inicio < datetime.now(): raise ValueError("Não pode no passado")
        self.__inicio = inicio        
    def set_duracao(self, duracao):
        if duracao < timedelta(0): raise ValueError("Não pode ser tempo negativo")
        self.__duracao = duracao   
    def get_filme(self): return self.__filme
    def get_inicio(self): return self.__inicio
    def get_duracao(self): return self.__duracao
    def fim(self): return self.__inicio + self.__duracao # datetime + timedelta -> datetime
    def __str__(self):
        return f"{self.__filme} {self.__inicio} {self.__duracao}"
    def to_json(self):
        dic = {}
        dic["filme"] = self.__filme
        dic["inicio"] = self.__inicio.strftime("%d/%m/%Y %H:%M")
        dic["duracao"] = self.__duracao.seconds
        return dic
    
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
        while op != 6:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.calcular()
            if op == 4: cls.abrir()
            if op == 5: cls.salvar()


    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Calcular, 4-Abrir, 5-Salvar, 6-Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        filme = input("Informe os dados da sessão do filme: ")
        inicio = datetime.strptime(input("Informe data e horário do filme: "), "%d/%m/%Y %H:%M")
        horas, minutos = map(int, input("Informe a duração hh:mm: ").split(":"))
        duracao = timedelta(hours=horas, minutes=minutos)
        c = Cinema(filme, inicio, duracao)
        cls.__objetos.append(c)

    @classmethod
    def listar(cls):
        for filme in cls.__objetos: print(filme)

    @classmethod
    def calcular(cls):
        m = cls.__objetos[0]
        for filme in cls.__objetos:
            if filme.get_duracao() > m.get_duracao(): m = filme
        print(m)    

    @classmethod
    def abrir(cls):
        pass

    @classmethod
    def salvar(cls):
        with open("filmes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Cinema.to_json)


UI.main()
