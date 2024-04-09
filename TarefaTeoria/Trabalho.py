from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_nos_parentes_proximos(tx, idade, nome, tipo):
    query = """
            CREATE (n:Pessoa:ParentesProximos {
            nome: $nome,
            idade: $idade,
            tipo: $tipo
})
        """
    result = tx.run(
        query,
        nome=nome,
        idade=idade,
        tipo=tipo
    )

    try:
        return [{"nome": row["n"]["description"]} for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def create_nos_parentes(tx, idade, nome, tipo):
    query = """
            CREATE (n:Pessoa:Parentes{
            nome: $nome,
            idade: $idade,
            tipo: $tipo
})
        """
    result = tx.run(
        query,
        nome=nome,
        idade=idade,
        tipo=tipo
    )

    try:
        return [{"nome": row["n"]["description"]} for row in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

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

quantidade_no = int(input('Entre com a quantidade de nós desejados: '))
quantidade_parentes_proximos = int(input())

# Verifica se a quantidade mínima de nós é atingida
if quantidade_no < 2:
    print("A quantidade mínima de nós é 10. Por favor, insira um número igual ou maior que 10.")
else:
    for x in range(quantidade_no):
        for y in range(quantidade_parentes_proximos):
            idade = int(input('Entre com a idade: '))
            nome = input('Entre com o nome: ')
            tipo = input('Entre com o tipo de parente: ')

            with driver.session() as session:
                session.execute_write(create_nos_parentes_proximos, idade, nome, tipo)

            with driver.session() as session:
                result = session.execute_read(get_amount_data)
                print(result[0]['amount'])

        for y in range(10-quantidade_parentes_proximos):
            idade = int(input('Entre com a idade: '))
            nome = input('Entre com o nome: ')
            tipo = input('Entre com o tipo de parente: ')

            with driver.session() as session:
                session.execute_write(create_nos_parentes, idade, nome, tipo)

            with driver.session() as session:
                result = session.execute_read(get_amount_data)
                print(result[0]['amount'])

driver.close()
