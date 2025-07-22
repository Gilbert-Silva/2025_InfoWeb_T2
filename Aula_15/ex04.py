import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

def salvar():    
    a = Cliente(1, "Alex")
    b = Cliente(2, "Danielle") 
    x = [a, b]
    with open("clientes.json", mode="w") as arquivo:
        json.dump(x, arquivo, default = vars)
    #arquivo.close()

def abrir():
    x = []
    with open("clientes.json", mode="r") as arquivo:
        lista = json.load(arquivo)
        for dic in lista:
            c = Cliente(dic["id"], dic["nome"])
            x.append(c)
    for c in x: print(c)

abrir()
            







