def calcular_preco_com_bonus(preco:float, entrega:bool):
    if entrega:
        return preco * 1.02
    return preco