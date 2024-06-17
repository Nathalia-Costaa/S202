from Database import Database
from writeAJson import writeAJson
from VendedorCLI import vendedorCLI
from VendedorDAO import vendedorDAO

db = Database(database="TrabalhoBD", collection="Loja")
vendedor = vendedorDAO(database=db)


vendedorCLI = vendedorCLI(vendedor)
vendedorCLI.run()

