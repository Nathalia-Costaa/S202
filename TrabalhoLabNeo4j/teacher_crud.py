class TeacherDatabase:
    def __init__(self, database):
        self.db = database

    def create_professor(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def get_professores(self, name):
        query = "MATCH (p:Teacher) RETURN p.name AS name, p.ano_nasc AS ano_nasc, p.cpf AS cpf"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def update_professor(self, name, newCpf) :
        query = "MATCH (p:Professor {name: $name}) SET p.cpf = $newCpf"
        parameters = {"name": name, "new_Cpf": newCpf}
        self.db.execute_query(query, parameters)

    def delete_professor(self, name):
        query = "MATCH (p:Teacher {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)