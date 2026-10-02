from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo):
         super().marca = marca
         super().modelo = modelo

    def cilindradas(self):
        return '344'