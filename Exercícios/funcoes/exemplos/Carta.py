class Carta:

    rementente:str
    destinario:str
    conteudo:str

    def __init__(self, remetente:str, destinario:str, conteudo:str):
        self.conteudo = conteudo
        self.destinatario = conteudo
        self.remetente= remetente

carta = Carta('João', 'Pietra', 'AAAAAAAAAAAAAAAA')
