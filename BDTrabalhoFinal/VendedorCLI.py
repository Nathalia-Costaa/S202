from Vendas import Vendas
from Vendedor import Vendedor
from Comprador import Comprador
from SimpleCLI import SimpleCLI

class vendedorCLI(SimpleCLI):
    def __init__(self, vendedor_model):
        super().__init__()
        self.vendedor_model = vendedor_model
        self.add_command("create", self.create_vendedor)
        self.add_command("read", self.read_vendedor)
        self.add_command("update", self.update_vendedor)
        self.add_command("delete", self.delete_vendedor)

    def create_vendedor(self):
        lista_vendas = []
        quant = int(input("Entre com a quantidade de vendas: "))
        for x in range(quant):
            nome_comprador = str(input("Entre com o nome do comprador: "))
            cpf = str(input("Entre com o cpf do comprador: "))
            telefone = str(input("Entre com o telefone do comprador: "))
            cidade = str(input("Entre com a cidade onde o comprador mora: "))
            idade = int(input("Entre com a idade do comprador: "))
            comprador = Comprador(nome_comprador, cpf, telefone, cidade, idade)

            valor = float(input("Entre com o valor da compra: "))
            forma_pagamento = str(input("Entre com a forma de pagamento: "))
            nome_produto = str(input("Entre com o nome do produto comprado: "))
            data_compra = str(input("Entre com a data da compra: "))

            venda = Vendas(valor, forma_pagamento, nome_produto, comprador, data_compra)

            lista_vendas.append(venda)

        nome = str(input("Entre com o nome do vendedor: "))
        porcentagem_comissao = float(input("Entre com a porcentagem de comissao (valores inteiros): "))

        vendedor = Vendedor(lista_vendas, nome, porcentagem_comissao)

        self.vendedor_model.create_vendedor_DAO(vendedor)

    def read_vendedor(self):
        id = input("Enter the id: ")
        vendedor = self.vendedor_model.read_vendedor_by_id(id)


    def update_vendedor(self):
        id = input("Enter the id: ")
        lista_vendas = []
        quant = int(input("Entre com a quantidade de vendas: "))
        for x in range(quant):
            nome_comprador = str(input("Entre com o nome do comprador: "))
            cpf = str(input("Entre com o cpf do comprador: "))
            telefone = str(input("Entre com o telefone do comprador: "))
            cidade = str(input("Entre com a cidade onde o comprador mora: "))
            idade = int(input("Entre com a idade do comprador: "))
            comprador = Comprador(nome_comprador, cpf, telefone, cidade, idade)

            valor = float(input("Entre com o valor da compra: "))
            forma_pagamento = str(input("Entre com a forma de pagamento: "))
            nome_produto = str(input("Entre com o nome do produto comprado: "))
            data_compra = str(input("Entre com a data da compra: "))

            venda = Vendas(valor, forma_pagamento, nome_produto, comprador, data_compra)

            lista_vendas.append(venda)

        nome = str(input("Entre com o nome do vendedor: "))
        porcentagem_comissao = int(input("Entre com a porcentagem de comissao (valores inteiros): "))

        vendedor = Vendedor(lista_vendas, nome, porcentagem_comissao)
        self.vendedor_model.update_vendedor(id, vendedor)

    def delete_vendedor(self):
        id = input("Enter the id: ")
        self.vendedor_model.delete_vendedor(id)

    def run(self):
        print("Welcome to the vendedor CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
