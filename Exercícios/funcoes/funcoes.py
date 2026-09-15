#Exercício 1
def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem-vindo(a) a {cidade}!"

#Exercicio 2
def calcular_perimetro(largura: float, altura: float):

    perimetro = 2 * (largura + altura)
    return perimetro

#Exercicio 3


if __name__=='__main__':
    
    print('EXERCICIOS =========================== \n\n')
    saudacao = formatar_saudacao('Alice','Porto Alegre')
    print(f'1 - {saudacao}')
    perimetro = calcular_perimetro(5, 10)
    print(f'2 - {perimetro}')
    print('\n\n=======================================')
