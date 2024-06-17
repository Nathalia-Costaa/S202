import Comprador


class Vendas:
    def __init__(self, valor, forma_pagamento, nome_produto, comprador, data_compra):
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.nome_produto = nome_produto
        self.comprador = comprador
        self.data_compra = data_compra
