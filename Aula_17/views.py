from models import Cliente, ClienteDAO

class View:
    @staticmethod
    def cliente_inserir(nome):
        ClienteDAO.inserir(Cliente(0, nome))

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()
    
