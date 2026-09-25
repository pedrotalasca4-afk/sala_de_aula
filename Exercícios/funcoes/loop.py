def dobrar(numeros:list):
    for numero in numeros:
        numero = numero * 2
        print(numero)

#Exercicio 1
def filtrar_pares(numeros:list):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        
    return pares

#Exercicio 2
def contar_negativos(numeros: list):
    count = 0
    for numero in numeros:
        if numero < 0:
            count+=1
    return count

#Exercicios 3 (Escreva uma função somar_maiores_que(numeros, limite) que receba uma lista de números e um valor de limite, retornando a soma apenas dos valores superiores ao limite.)
def somar_maiores_que(numeros:list, limite:int):
    maior = 0
    for numero in numeros:
        if numero > limite:
            maior+=numero
    return maior

#Exercicio 4 (Escreva uma função zerar_negativos(numeros) que receba uma lista de inteiros e retorne uma nova lista onde todo número negativo é substituído por 0.)
def zerar_negativos(numeros:list):
    novo_negativo = numeros.copy()
    for numero in novo_negativo:
        if numero< 0 :
            indice = numeros.index(numero)
            novo_negativo[indice] = 0
            
    return novo_negativo

#Exercicio 5 (Escreva uma função contem_valor(lista, alvo) usando um laço while para verificar se o valor alvo está presente na lista. Retorne True ou False.)
def contem_valor(lista:list, alvo:str):
    while alvo in lista:
        return 'True'
    else:
        return 'False'
    
#Exercicio 6 (Escreva uma função contar_aprovados(notas) que receba uma lista de notas e retorne quantos alunos obtiveram nota maior ou igual a 7.0.)
def contar_aprovados(notas:list):
    aprovados = 0
    for nota in notas:
        if nota >= 7.0:
            aprovados += 1
    return aprovados

#Exercicio 7 (Escreva uma função filtrar_palavras_curtas(palavras, tamanho_maximo) que receba uma lista de strings e retorne apenas as palavras com comprimento menor ou igual ao tamanho_maximo.)
def filtrar_palavras_curtas(palavras:list, tamanho_maximo:int):
    menores = []
    for palavra in palavras:
        if len(palavra) <= tamanho_maximo:
            menores.append(palavra)
    return menores

#Exercicio 8 (Escreva uma função separar_pares_impares(numeros) que receba uma lista de inteiros e retorne uma string no formato "Pares: X | Ímpares: Y", onde X é a quantidade de pares e Y a quantidade de ímpares.)
def separar_pares_impares(numeros:list):
    pares = []
    impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
            len(pares)
        if numero % 2 != 0:
            impares.append(numero)
            len(impares)

    return f'Pares : {len(pares)} | Impares : {len(impares)}'

#Exercicio 9 (Escreva uma função encontrar_extremos(numeros) que receba uma lista não vazia de números e retorne uma tupla (menor, maior) sem utilizar min() ou max().)
def encontrar_extremos(numeros:list):
    

if __name__=='__main__':
    dobrar([1,2,3,4,5])
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6,])
    print(f'1 - {numeros_pares}')
    negativos = contar_negativos([10, -3, 0, -5, 8, -1])
    print(f'2 - {negativos}')
    s_maiores = somar_maiores_que([10, 5, 20, 3, 15], 8)
    print(f'3 - {s_maiores}')
    z_negativos = zerar_negativos([4, -2, 7, -9, 0])
    print(f'4 - {z_negativos}')
    pega_banana = contem_valor(["maçã", "banana", "uva"], "banana")
    print(f'5 - {pega_banana}')
    aprovados = contar_aprovados([8.5, 5.0, 7.0, 6.5, 9.0])
    print(f'6 - {aprovados}')
    p_curtas = filtrar_palavras_curtas(["sol", "computador", "python", "mar"], 6)
    print(f'7 - {p_curtas}')
    separar = separar_pares_impares([1, 2, 3, 4, 5])
    print(f'8 - {separar}')
    extremo = encontrar_extremos([14, 2, 35, -4, 20])
    print(f'9 - {extremo}')