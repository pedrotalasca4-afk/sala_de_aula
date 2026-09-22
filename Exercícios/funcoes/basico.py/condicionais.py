def fizz_buzz(numero=int):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'fizzbuzz'
    elif numero % 3 == 0:
        return 'fizz'
    elif numero % 5 == 0:
        return 'buzz'
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
    if cliente_vip or valor_compra > 200:
        valor_final_d = valor_compra * 0.15
        desconto1 = valor_compra - valor_final_d
        return f'Valor Final: {desconto1:.2f}'


    valor_final_sd = valor_compra * 0.05
    desconto2 = valor_compra - valor_final_sd
    return f'Valor Final: {desconto2:.2f}'
   
#Exercicio 7
def conceito_nota(nota:float):
    if nota >= 9:
        return 'A'
    if nota >= 7:
        return 'B'
    if nota >= 5:
        return 'C'
    return 'F'
   
#Exercicio 8
def tipo_triangulo(a:int, b:int, c:int):
    if not ((a + b > c) and (b + c > a) and (c + a > b)):
        return 'Não é um triângulo'


    if a == b == c:
        return 'Equilatero'
    if a == b or b == c or a == c:
        return 'Isóceles'
    return 'Escaleno'


#Exercicio 9
def calcular_imposto(salario:float):
    if salario < 2000.00:
        imposto1 = 0
        return imposto1
    if  salario > 2000.00:
        imposto2 = (salario - 2000) * 0.10
        return imposto2
    if salario > 4000.00:
        imposto3 = (2000*10) + (salario - 4000) * 20
        return imposto3
       
#Exercicio 10
def e_bissexto(ano:int):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return 'True'
    else:
        return 'False'


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
    trian = tipo_triangulo(2, 5, 59)
    print(f'8 - {trian}')
    imp = calcular_imposto(3000.0)
    print(f'9 - {imp}')
    bissexto = e_bissexto(1900)
    print(f'10 - {bissexto}')
    pass