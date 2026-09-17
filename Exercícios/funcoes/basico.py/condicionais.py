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
    pass