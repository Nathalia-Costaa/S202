from Database import Database
from writeAJson import writeAJson
from MotoristaCLI import motoristaCLI
from MotoristaDAO import MotoristaDAO

db = Database(database="relatorio_05", collection="Motoristas")
motorista = MotoristaDAO(database=db)


motoristaCLI = motoristaCLI(motorista)
motoristaCLI.run()