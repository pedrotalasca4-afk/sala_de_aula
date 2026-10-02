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

#Exercício 11:
# Objetivo: Escreva uma função avaliar_estudante(p1, p2, frequencia, entregou_trabalho_extra).
# Cálculo da Média: media = (p1 + p2) / 2
# Regras de Avaliação:
#       Se frequencia < 75: Retorne "Reprovado por Frequência".
#       Se frequencia >= 75:
            # Se media >= 7.0: Retorne "Aprovado Direto".
            # Se media estiver entre 5.0 e 6.9: Se entregou_trabalho_extra == True, adicione  +1.0 ponto à média. Se a nova média for >= 7.0, retorne "Aprovado com Trabalho Extra"; caso contrário, retorne "Exame Final".
            # Se media < 5.0: Retorne "Reprovado por Nota".
# Exemplos:
    # avaliar_estudante(6.0, 6.5, 80, True) → "Aprovado com Trabalho Extra"
    # avaliar_estudante(8.0, 9.0, 70, False) → "Reprovado por Frequência"
def avaliar_estudante(p1:float, p2: float, frequencia:int, entregou_trabalho_extra:bool):
    media = (p1 + p2) / 2
    if frequencia < 75:
        return 'Reprovado por Frequência'
    if frequencia >= 75:
        if media >= 7.0:
            return 'Aprovado Direto'
        if media > 5.0 and media < 6.9:
            if entregou_trabalho_extra == True:
                media += 1.0
                if media >= 7.0:
                    return 'Aprovado com Trabalho Extra'
                else:
                    return 'Exame Final'
        if media < 5.0:
            return 'Reprovado por Nota'

#Exercicio 12
#Objetivo: Escreva uma função localizar_ponto(x, y) que determine a posição exata de um ponto no plano cartesiano 2D sem usar laços ou vetores.
#Regras:
    #x == 0 e y == 0 → "Origem"
    #x == 0 e y != 0 → "Eixo Y"
    #x != 0 e y == 0 → "Eixo X"
    #x > 0 e y > 0 → "Q1"
    #x < 0 e y > 0 → "Q2"
    #x < 0 e y < 0 → "Q3"
    #x > 0 e y < 0 → "Q4"
#Exemplos:
    #localizar_ponto(0, -5) → "Eixo Y"
    #localizar_ponto(-3, -4) → "Q3"
def localizar_ponto(x:int,y:int):
     if x== 0 and y == 0:
         return 'Origem'
     if x == 0 and y != 0:
         return 'Eixo Y'
     if x != 0 and y == 0:
         return 'Eixo X'
     if x > 0 and y > 0:
         return 'Q1'
     if x < 0 and y > 0:
         return 'Q2'
     if x < 0 and y < 0:
         return 'Q3'
     if x > 0 and y < 0:
         return 'Q4'
     
# Exercício 13: Simulador de Tarifação Telefônica em Rolo
# Objetivo: Escreva uma função calcular_fatura_telefone(minutos, gigas, e_estudante).
# Regras de Cobrança:
    # Plano Base: R$ 50.00 (inclui até 100 minutos e até 5 GB).
    # Minutos excedentes (acima de 100 min): R$ 0.50 por minuto adicional.
    # Dados excedentes (acima de 5 GB): R$ 10.00 por GB adicional.
    # Regra de Desconto: Se e_estudante == True E o valor total da fatura (com excedentes) for estritamente superior a R$ 100.00, aplique um desconto de R$ 20.00.
# Retorno: Retorne uma f-string formatada (ex: "Fatura Final: R$ X.XX").
# Exemplos:
    # calcular_fatura_telefone(120, 7, True) → "Fatura Final: R$ 60.00" (Cálculo: R$ 50 + 200.50 + 210 = R$ 80; como não passou de R$ 100, não aplica o desconto)
    # calcular_fatura_telefone(200, 10, True) → "Fatura Final: R$ 130.00" (Cálculo: R$ 50 + 1000.50 + 510 = R$ 150 - R$ 20 = R$ 130)
def calcular_fatura_telefone(minutos: int, gigas:int, e_estudante:bool):


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
    estudante = avaliar_estudante(8.0, 9.0, 70, False)
    print(f'11 - {estudante}')
    ponto = localizar_ponto(-3, -4)
    print(f'12 - {ponto}')
    pass