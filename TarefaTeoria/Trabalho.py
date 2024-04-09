from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def consultar_parentes_homens(tx):
    query = """
        MATCH (p:Pessoa:Parente {sexo: 'M'})
        RETURN COUNT(p) AS quantidade
    """
    result = tx.run(query)
    return result.single()["quantidade"]

# Função para consultar os irmãos
def consultar_irmaos(tx):
    query = """
        MATCH (p1:Pessoa)-[:IRMAO_DE]->(p2:Pessoa)
        RETURN p1.nome AS nome1, p2.nome AS nome2
    """
    result = tx.run(query)
    return [(record["nome1"], record["nome2"]) for record in result]

# Função para consultar o número de parentes com mais de 25 anos
def consultar_parentes_mais_de_25_anos(tx):
    query = """
        MATCH (p:Pessoa:Parente)
        WHERE p.idade > 25
        RETURN COUNT(p) AS quantidade
    """
    result = tx.run(query)
    return result.single()["quantidade"]

def create_nos_parentes_proximos(tx, idade, nome, sexo):
    query = """
            CREATE (n:Pessoa:ParentesProximos {
            nome: $nome,
            idade: $idade,
            sexo: $sexo
})
        """
    result = tx.run(
        query,
        nome=nome,
        idade=idade,
        sexo=sexo
    )

    try:
        return [{"nome": row["n"]["description"]} for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


def create_nos_parentes(tx, idade, nome, sexo):
    query = """
            CREATE (n:Pessoa:Parentes{
            nome: $nome,
            idade: $idade,
            sexo: $sexo
})
        """
    result = tx.run(
        query,
        nome=nome,
        idade=idade,
        sexo=sexo
    )

    try:
        return [{"nome": row["n"]["description"]} for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


def criar_relacionamento_irmao_de(tx, nome1, nome2):
    query = """
        MATCH (p1:Pessoa {nome: $nome1}), (p2:Pessoa {nome: $nome2})
        CREATE (p1)-[:IRMAO_DE]->(p2)
    """
    tx.run(query, nome1=nome1, nome2=nome2)


# Função para criar relacionamentos "namorado_de"
def criar_relacionamento_namorado_de(tx, nome1, nome2, propriedade):
    query = """
        MATCH (p1:Pessoa {nome: $nome1}), (p2:Pessoa {nome: $nome2})
        CREATE (p1)-[:NAMORADO_DE {propriedade: $propriedade}]->(p2)
    """
    tx.run(query, nome1=nome1, nome2=nome2, propriedade=propriedade)


# Função para criar relacionamentos "pai_de"
def criar_relacionamento_pai_de(tx, nome_pai, nome_filho):
    query = """
        MATCH (pai:Pessoa {nome: $nome_pai}), (filho:Pessoa {nome: $nome_filho})
        CREATE (pai)-[:PAI_DE]->(filho)
    """
    tx.run(query, nome_pai=nome_pai, nome_filho=nome_filho)


# Função para criar relacionamentos "familiar_distante_de"
def criar_relacionamento_familiar_distante_de(tx, nome1, nome2):
    query = """
        MATCH (p1:Pessoa {nome: $nome1}), (p2:Pessoa {nome: $nome2})
        CREATE (p1)-[:FAMILIAR_DISTANTE_DE]->(p2)
    """
    tx.run(query, nome1=nome1, nome2=nome2)


def get_amount_data(tx):
    query = """
        MATCH(n:Pessoa:Parentesco) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{'amount': row['amount']} for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


uri = "neo4j+s://70eb9cb8.databases.neo4j.io"
user = "neo4j"
password = "ZuRRw36-NQKZBFQxuIwj-QjU00A516BxJ_zsGv23D7Y"

driver = GraphDatabase.driver(uri, auth=(user, password))

print('--------------------------SEJA BEM VINDO AO GRAFO DA FAMILIA--------------------------')
print('Caso seja a sua primeira vez no sistema peço que você primeiro se cadastre, alem disso sempre escreva o seu nome'
      ' exatamente como no cadastrado')

nome_eu = input('Primeiramente entre com o seu nome: ')
quantidade_no = int(input('Entre com a quantidade de nós desejados: '))
quantidade_parentes_proximos = int(input('Entre com a quantidade de parentes proximos: '))

# Verifica se a quantidade mínima de nós é atingida
if quantidade_no < 10:
    print("A quantidade mínima de nós é 10. Por favor, insira um número igual ou maior que 10.")
else:
    for y in range(quantidade_parentes_proximos):
        idade = int(input('Entre com a idade: '))
        nome = input('Entre com o nome: ')
        sexo = input('Entre com o sexo (M ou F): ')

        tipo = input('Entre com o tipo de parente: pai, irmao, namorado ou eu '
                     '(escreva como está escrito aqui, por favor) ')

        with driver.session() as session:
            session.execute_write(create_nos_parentes_proximos, idade, nome, sexo)

        with driver.session() as session:
            result = session.execute_read(get_amount_data)
            print(result[0]['amount'])

        with driver.session() as session:
            if tipo == 'eu':
                continue
            elif tipo == 'irmao':
                session.execute_write(criar_relacionamento_irmao_de, nome_eu, nome)
            elif tipo == 'namorado':
                desde = int(input("Desde que ano voces namoram? Digite somente o numero"))
                session.execute_write(criar_relacionamento_namorado_de, nome_eu, nome, desde)
            elif tipo == 'pai':
                session.execute_write(criar_relacionamento_pai_de, nome_eu, nome)

    for y in range(quantidade_no - quantidade_parentes_proximos):
        idade = int(input('Entre com a idade: '))
        nome = input('Entre com o nome: ')
        sexo = input('Entre com sexo (M ou F): ')

        with driver.session() as session:
            session.execute_write(create_nos_parentes, idade, nome, sexo)

        with driver.session() as session:
            result = session.execute_read(get_amount_data)
            print(result[0]['amount'])

        with driver.session() as session:
                session.execute_write(criar_relacionamento_familiar_distante_de, nome, nome_eu)

print("-------------- Aqui esta algumas informações com base nos dados obtidos: --------------")
with driver.session() as session:
    # Consultar o número de parentes que são homens
    quantidade_homens = session.execute_read(consultar_parentes_homens)
    print(f"Quantidade de parentes que são homens: {quantidade_homens}")
    print('----------')

    # Consultar os irmãos
    print("Irmãos:")
    irmaos = session.execute_read(consultar_irmaos)
    for nome1, nome2 in irmaos:
        print(f"{nome1} é irmão de {nome2}")
    print('----------')

    # Consultar o número de parentes com mais de 25 anos
    quantidade_mais_de_25_anos = session.execute_read(consultar_parentes_mais_de_25_anos)
    print(f"Quantidade de parentes com mais de 25 anos: {quantidade_mais_de_25_anos}")
    print('----------')

driver.close()
