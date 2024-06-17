from pymongo import MongoClient
from bson.objectid import ObjectId

import Vendedor


class vendedorDAO:
    def __init__(self, database):
        self.db = database

    def create_vendedor_DAO(self, vendedor: Vendedor):
        try:
            vendedor_doc = {
                "nome": str(vendedor.nome),
                "porcentagem_comissao": int(vendedor.comissao),
                "vendas": [{
                    "valor": float(vendas.valor),
                    "forma_pagamento": str(vendas.forma_pagamento),
                    "nome_produto": str(vendas.nome_produto),
                    "data_compra": str(vendas.data_compra),
                    "comprador": {
                        "nome": vendas.comprador.nome,
                        "cpf": vendas.comprador.cpf,
                        "telefone": vendas.comprador.telefone,
                        "cidade": vendas.comprador.cidade,
                        "idade": vendas.comprador.idade
                    }
                } for vendas in vendedor.vendas]
            }

            res = self.db.collection.insert_one(vendedor_doc)
            print(f"vendedor created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating vendedor: {e}")
            return None

    def read_vendedor_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"vendedor found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading vendedor: {e}")
            return None

    def update_vendedor(self, id: str, vendedor: Vendedor):
        try:
            vendedor_doc = {
                "$set": {
                    "nome": str(vendedor.nome),
                    "porcentagem_comissao": int(vendedor.comissao),
                    "vendas": [{
                        "valor": float(vendas.valor),
                        "forma_pagamento": str(vendas.forma_pagamento),
                        "nome_produto": str(vendas.nome_produto),
                        "data_compra": str(vendas.data_compra),
                        "comprador": {
                            "nome": vendas.comprador.nome,
                            "cpf": vendas.comprador.cpf,
                            "telefone": vendas.comprador.telefone,
                            "cidade": vendas.comprador.cidade,
                            "idade": vendas.comprador.idade
                        }
                    } for vendas in vendedor.vendas]
                }
            }

            res = self.db.collection.update_one({"_id": ObjectId(id)}, vendedor_doc)
            print(f"vendedor updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating vendedor: {e}")
            return None

    def delete_vendedor(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"vendedor deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting vendedor: {e}")
            return None
