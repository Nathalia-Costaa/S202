from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

print("----------------------------------------------------")

# 1- Total gasto por dia:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
])
for data in result:
    print(f"Data: {data['_id']} - Total de vendas: R${data['total_vendas']:.2f}")

writeAJson(result, "Total gosto por dia")

print("----------------------------------------------------")

# 2 - Produto mais vendido em todas as compras.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total_vendido": -1}},
    {"$limit": 1}
])

for produto in result:
    print(f"Produto mais vendido: {produto['_id']} - Total vendido: {produto['total_vendido']} unidades")

print("----------------------------------------------------")

# 3 - Cliente que mais gastou em uma única compra.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"total_gasto": -1}},
    {"$limit": 1}
])

for cliente in result:
    print(f"Cliente que mais gastou: {cliente['_id']} - Total gasto: R${cliente['total_gasto']:.2f}")

print("----------------------------------------------------")

# 4 - Produtos que tiveram uma quantidade vendida acima de 1 unidades.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
    {"$match": {"total_vendido": {"$gt": 1}}}
])

for produto in result:
    print(f"Produto: {produto['_id']} - Total vendido: {produto['total_vendido']} unidades")

print("----------------------------------------------------")