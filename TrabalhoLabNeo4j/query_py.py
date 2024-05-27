from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def procurar_renzo(tx):
    query = """
        MATCH (p:Teacher {name: 'Renzo'})
        RETURN p.ano_nasc AS ano_nasc, p.cpf AS cpf
    """
    result = tx.run(query)
    return result.single()["infos_renzo"]


def procurar_prof_m(tx):
    query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name AS name, t.CPF AS CPF
    """
    result = tx.run(query)
    return result.single()["infos_prof_m"]


def procurar_cidades(tx):
    query = """
        MATCH (t:City)
        RETURN t.name AS name
    """
    result = tx.run(query)
    return result.single()["cidades"]

def procurar_escolas(tx):
    query = """
        MATCH (t:School)
        WHERE t.number >= 150 and t.number <= 550 
        RETURN t.name AS name, t.address AS address, t.number AS number
    """
    result = tx.run(query)
    return result.single()["escolas"]

def idade_professores(self):
    query = """
    MATCH (t:Teacher)
    WITH MIN(t.ano_nasc) AS mais_jovem, MAX(t.ano_nasc) AS mais_velho
    RETURN mais_jovem, mais_velho
    """
    result = self.db.execute_query(query)
    return result

def media_habitantes(tx):
    query = """
        MATCH (t:City)
        RETURN AVG(t.population) AS population
    """
    result = tx.run(query)
    return result.single()["populacao"]

def procurar_cidade(tx):
    query = """
        MATCH (t:City {cep: '37540-000'})
        RETURN REPLACE(t.name, 'a', 'A') AS name
    """
    result = tx.run(query)
    return result.single()["cidade"]

def procurar_caracter_nomes(tx):
    query = """
        MATCH (t:Teacher)
        RETURN substring(t.name, 2, 1) AS terceiro_caractere
    """
    result = tx.run(query)
    return result.single()["caracteres"]

