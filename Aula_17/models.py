import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        id = 0
        for aux in cls.__objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1
        cls.__abrir()    
        cls.__objetos.append(obj)
        cls.__salvar()

    @classmethod
    def listar(cls):
        cls.__abrir()    
        return cls.__objetos

    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = Cliente(dic["id"], dic["nome"])
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass             

    @classmethod
    def __salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = vars)

    
