import enum

class Pagamento(enum.Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2

class Boleto:
    def __init__(self, valor):
        self.__valor_boleto = valor
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EmAberto    
    def pagar(self, valor_pago):
        if valor_pago == self.__valor_boleto:
            self.__situacao_pagamento = Pagamento.Pago
    def situacao(self):
        return self.__situacao_pagamento

x = Boleto(100)
print(x.situacao())
x.pagar(100)
print(x.situacao())


