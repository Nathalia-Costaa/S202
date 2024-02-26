from Aluno import Aluno
from Aula import Aula
from Professor import Professor

professor = Professor("Victor")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Nathalia")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())
