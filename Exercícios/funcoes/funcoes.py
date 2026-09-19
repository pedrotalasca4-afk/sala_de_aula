#Exercício 1
def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem-vindo(a) a {cidade}!"

#Exercicio 2
def calcular_perimetro(largura: float, altura: float):

    perimetro = 2 * (largura + altura)
    return perimetro

#Exercicio 3
def fahrenheit_para_celsius(temp_f:float):
    temp_c =(temp_f-32)*(5/9)
    return temp_c

#Exercício 4
def calcular_gorjeta_por_pessoa(conta:float, porcentagem_gorjeta:int, pessoas:int):
    gorjeta = (conta*(porcentagem_gorjeta/100))/(pessoas)
    return gorjeta

#Exercício 5
def  resumo_circulo(raio:int):
    pi=3.14159
    area=(pi * raio**2)
    return f'Um círculo com raio {raio} tem uma área de {area:.2f}'

#Exercício 6
def resumo_juros_compostos(capital:float, taxa:float, anos:int):
    juros_compostos = capital*(1+taxa/100)**anos
    return f'Após {anos} anos, R$ {capital} cresce para {juros_compostos:.2f}.'

#Exercício 7
def metricas_cilindro(raio:float, altura:float):
    V_cilin= (3.14159*raio**2*altura)
    A_Base=(2*(3.14159*raio**2)+2*3.14159*raio*altura)
    return f'Volume do Cilindro: {V_cilin:.2f} | Área de Superfície: {A_Base:.2f}'

#Exercício 8
def gerar_item_fatura(nome_item:str, preco:float, porcentagem_desconto:float):
    desconto = (preco*(porcentagem_desconto/100))
    preco_final = preco - desconto
    return f'{nome_item} | Preço Final: R$ {preco_final} (Você economizou R$ {desconto}) '

#Exercicio 9 
def resumo_emprestimo(capital:float, taxa_anual:float, anos:int):
    r = taxa_anual / 12 / 100
    n = anos * 12
    Mensal = capital * (r * ((1+r) ** n)) / (((1 + r) ** n) - 1)
    pag_total = Mensal * n

    return f"Empréstimo: R$ {capital} Parcela Mensal: R$ {Mensal:.2f} | Total Pago: R$ {pag_total:.2f}"

#Exercicio 10

import math
def calcular_distancia(x1:int, y1:int, x2:int, y2:int):
    d = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
    return f'A distância entre ({x1},{y1}) e ({x2},{y2}) é de {d} unidades'


if __name__=='__main__':
    
    print('EXERCICIOS =========================== \n\n')
    saudacao = formatar_saudacao('Alice','Porto Alegre')
    print(f'1 - {saudacao}')
    perimetro = calcular_perimetro(5, 10)
    print(f'2 - {perimetro}')
    print(f'3 - {fahrenheit_para_celsius(68)}')
    print(f'4 - {calcular_gorjeta_por_pessoa(100.0, 15, 3)}')
    Circulo = resumo_circulo(3.0)
    print(f'5 -{Circulo}')
    Juros = resumo_juros_compostos(1000.0, 5.0, 3)
    print(f'6 - {Juros}')
    Cilindro = metricas_cilindro(2.0, 5.0)
    print(f'7 - {Cilindro}')
    Fatura = gerar_item_fatura("Item: Teclado", 80.0, 15.0)
    print(f'8 - {Fatura}')
    emprestimo = resumo_emprestimo(10000, 6.0, 3)
    print(f'9 - {emprestimo}')
    distancia = calcular_distancia(1, 2 , 4, 6)
    print(f'10 - {distancia}')
    print('\n\n=======================================')
