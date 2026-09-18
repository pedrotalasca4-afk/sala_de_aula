def fizz_buzz(numero=int):
    if numero % 3 ==0:
        return 'fizzbuz'
    elif numero % 5 ==0:
        return 'buzz'
    elif numero % 3 == 0 and numero % 5 == 0:
        return 'fizz'
    else:
        return numero

#Exercicio 1
def verificar_maioridade(idade:int):
    if idade >= 18:
        return 'Maior de idade'
    else:
        return 'Menor de idade'

#Exercicio 2
def verificar_paridade(numero:int):
    if numero % 2 ==0:
        return 'Par'
    else:
        return 'Impar'
    
#Exercicio 3
def classificar_numero(numero:float):
    if numero > 0:
        return 'Positivo'
    if numero < 0:
        return 'Negativo'
    if numero == 0:
        return 'Zero'
    
#Exercicio 4
def calcular_resultado(nota1:float, nota2:float):
    resultado = (nota1+nota2)/2
    if resultado >= 7:
        return 'Aprovado'
    if resultado < 7:
        return 'Reprovado'
    
#Exercicio 5
def maior_de_dois(a:int, b:int):
    if a > b:
        return 'O primeiro é maior'
    if a < b:
        return 'O segundo é maior'
    if a == b:
        return 'São iguais'
    
#Exercicio 6
def calcular_desconto(valor_compra:float, cliente_vip:bool):
    if cliente_vip == True or valor_compra > 200:
        valor_final_d = (valor_compra*(15/100))
        desconto1 = valor_compra - valor_final_d
        return f'Valor Final: {desconto1:.2f}'
    
    if cliente_vip == False or valor_compra < 200:
        valor_final_sd = (valor_compra*(5/100))
        desconto2 = valor_compra - valor_final_sd
        return f'Valor Final: {desconto2:.2f}'
    
#Exercicio 7
def conceito_nota(nota:float):
    if nota >=9 or nota >=10:
        return 'A'
    if nota >=7 or nota >=8.9:
        return 'B'
    if nota >=5 or nota >=6.9:
        return 'C'
    if nota <5:
        return 'F'
    
#Exercicio 8
def tipo_triangulo(a:int, b:int, c:int):
    if (a+b>c) and (a+c>b) and (c+a>b):
        if a==b==c:
        return 'Equilátero'

if __name__=='__main__':
    teste = fizz_buzz(85)
    print(f'{teste}')
    verif = verificar_maioridade(10)
    print(f'1 - {verif}')
    parouimpar = verificar_paridade(3)
    print(f'2 - {parouimpar}')
    classn = classificar_numero(-3)
    print(f'3 - {classn}')
    resul = calcular_resultado(5.0, 6.5)
    print(f'4 - {resul}')
    Comp = maior_de_dois(5, 5)
    print(f'5 - {Comp}')
    cdes = calcular_desconto(100.0, False)
    print(f'6 - {cdes}')
    nota = conceito_nota(4.2)
    print(f'7 - {nota}')
    pass