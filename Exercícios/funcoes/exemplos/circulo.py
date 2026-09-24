class Circulo:

    raio:int

    def __init__(self,
                 raio:int):
        self.raio = raio if raio < 10 else 10

circulo = Circulo(12)