from Corrida import Corrida
from Motorista import Motorista
from Passageiro import Passageiro
from SimpleCLI import SimpleCLI

class PersonCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.create_person)
        self.add_command("read", self.read_person)
        self.add_command("update", self.update_person)
        self.add_command("delete", self.delete_person)

    def create_corrida(self):
        id_motorista = int(input("Entre com o id do motorista"))

        nota_corrida = int(input("Entre com a nota da corrida: "))
        distancia_corrida = float(input("Entre com a distancia da corrida: "))
        valor = float(input("Entre com o valor da distancia: "))
        nome_passageiro = input("Entre com o nome do passageiro: ")
        documento = input("Entre com o documento do passageiro")

        passageiro = Passageiro(nome_passageiro, documento)
        corrida = Corrida(nota_corrida, distancia_corrida, valor, passageiro)

        self.MotoristaDAO.create_corrida(id_motorista, corrida)

    def create_motorista(self):
        nota_motorista = int(input("Entre com a nota do motorista: "))
        self.MotoristaDAO.create_motorista(nota_motorista)


    def read_person(self):
        id = input("Enter the id: ")
        person = self.MotoristaDAO.read_person_by_id(id)
        if person:
            print(f"Name: {person['name']}")
            print(f"Age: {person['age']}")

    def update_person(self):
        id = input("Enter the id: ")
        name = input("Enter the new name: ")
        age = int(input("Enter the new age: "))
        self.MotoristaDAO.update_person(id, name, age)

    def delete_person(self):
        id = input("Enter the id: ")
        self.MotoristaDAO.delete_person(id)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
