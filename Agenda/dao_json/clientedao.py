import json
from dao_json.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Cliente.to_json) 