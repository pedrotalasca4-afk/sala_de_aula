def calcular_preco_com_bonus(preco:float, entrega:bool):
    if preco < 0:
        raise ValueError('Não se aceita preco negativo')
    
    if entrega:
        return preco * 1.02
    return preco