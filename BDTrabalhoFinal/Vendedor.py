import Vendas

class Vendedor:
    def __init__(self, vendas, nome, comissao):
        self.vendas = vendas
        self.nome = nome
        self.comissao = comissao
    def adicionar_corrida(self, vendas):
        self.vendas.append(vendas)
