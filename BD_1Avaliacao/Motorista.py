import Corrida


class Motorista:
    def __init__(self, nota):
        self.corrida = []
        self.nota = nota
    def adicionar_corrida(self, corrida):
        self.corrida.append(corrida)
