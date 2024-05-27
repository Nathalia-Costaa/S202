class TeacherDatabase:
    def __init__(self, database):
        self.db = database

    def create_professor(self, name, ano_nasc, cpf):
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def get_professores(self, name=None):
        query = """
        MATCH (p:Teacher)
        """
        if name:
            query += " WHERE p.name = $name"
        query += " RETURN p.name AS name, p.ano_nasc AS ano_nasc, p.cpf AS cpf"
        parameters = {"name": name} if name else None
        results = self.db.execute_query(query, parameters)
        return results

    def update_professor(self, name, newCpf):
        query = """
        MATCH (p:Teacher {name: $name})
        SET p.cpf = $newCpf
        RETURN p
        """
        parameters = {"name": name, "newCpf": newCpf}
        result = self.db.execute_query(query, parameters)
        if result:
            return f"CPF do professor {name} atualizado com sucesso para {newCpf}."
        else:
            return f"Professor {name} não encontrado."

    def delete_professor(self, name):
        query = """
        MATCH (p:Teacher {name: $name})
        DETACH DELETE p
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
