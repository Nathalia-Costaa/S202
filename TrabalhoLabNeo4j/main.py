from database import Database
from teacher_crud import TeacherDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("neo4j+s://fc39d5cf.databases.neo4j.io", "neo4j", "aAimDknf3beishTTQrBCCJAvCoN_kxBCRFBvCZpGa1s")
db.drop_all()

# Criando uma instância da classe TeacherDatabase para interagir com o banco de dados
teacher_db = TeacherDatabase(db)

teacher_db.create_professor("Chris Lima", 1956, "189.052.396-66")

print("Informações: Chris Lima: \n")
print(teacher_db.get_professores("Chris Lima"))

print("Atualiazando cpf: Chris Lima: \n")
teacher_db.update_professor("Chris Lima", "189.052.396-66")



# Fechando a conexão com o banco de dados
db.close()