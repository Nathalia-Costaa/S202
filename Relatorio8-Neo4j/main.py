from Neo4jGameDatabase import Neo4jGameDatabase

# Conectando ao banco de dados
db = Neo4jGameDatabase("bolt://34.205.247.223:7687", "neo4j", "parities-peacetime-frequency")

# Criando jogadores
db.create_player(1, "Alice")
db.create_player(2, "Bob")
db.create_player(3, "Charlie")

# Criando uma partida
db.create_match(1, "Alice ganhou", [1, 2])

# Obtendo a lista de jogadores
players = db.get_players()
print("Lista de jogadores:")
for player in players:
    print(player)

# Obtendo informações sobre uma partida específica
match_info = db.get_match(1)
print("\nInformações da partida 1:")
print(match_info)

# Obtendo o histórico de partidas de um jogador
player_history = db.get_player_history(1)
print("\nHistórico de partidas de Alice:")
for match in player_history:
    print(match)

# Fechando a conexão com o banco de dados
db.close()
