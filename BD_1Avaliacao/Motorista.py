import Corrida


class Motorista:
    def __init__(self, nota, corrida):
        self.corrida = corrida
        self.nota_motorista = nota
    def adicionar_corrida(self, corrida):
        self.corrida.append(corrida)
