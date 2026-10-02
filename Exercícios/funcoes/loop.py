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
def encontrar_extremos(numeros):
    maior = numeros[0]
    menor = numeros[0]


    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return f'({menor},{maior})'


#Exercício 10: Processamento de Caixa Eletrônico com while
#Objetivo: Escreva uma função simular_saque(saldo_inicial, saques) que receba o saldo da conta e uma lista de saques desejados. Processa cada saque sequencialmente usando while. Se o saldo for suficiente, desconta o valor; se não for, ignora o saque. Retorne o saldo restante.
#Exemplo de Chamada: simular_saque(200, [50, 100, 80, 30])
#Retorno Esperado: 20 (Subtrai 50, 100 e 30; ignora o 80 por saldo insuficiente)
def simular_saque(saldo_inicial:int, saques:list):
    for saque in saques:
        while saldo_inicial > saque:
            saldo_inicial -= saque
    return saldo_inicial


#Exercício 11: Remover Duplicados Mantedor de Ordem
#Objetivo: Escreva uma função remover_duplicados(lista) que receba uma lista e retorne uma nova lista apenas com a primeira ocorrência de cada elemento, preservando a ordem original.
#Exemplo de Chamada: remover_duplicados([1, 3, 2, 3, 1, 4, 2])
#Retorno Esperado: [1, 3, 2, 4]
def remover_duplicados(lista:list):
    nao_d = []
    for numero in lista:
        if numero not in nao_d:
            nao_d.append(numero)
    return nao_d


#Exercício 12: Média dos Positivos
# Objetivo: Escreva uma função media_positivos(numeros) que calcule a média aritmética apenas dos números estritamente positivos. Se não houver números positivos, retorne 0.0.
# Exemplo de Chamada: media_positivos([-5, 10, -2, 20, 30])
# Retorno Esperado: 20.0 (10 + 20 + 30) / 3
def media_positivos(numeros:list):
    positivos = []
    for numero in numeros:
        if numero > 0:
            positivos.append(numero)
            total = sum(positivos) / len(positivos)
    return total


#Exercício 13: Validador de Senhas em Lista
# Objetivo: Escreva uma função validar_senhas(lista_senhas) que receba uma lista de strings e retorne apenas as senhas que possuem pelo menos 8 caracteres.
# Exemplo de Chamada: validar_senhas(["12345", "senha1234", "admin", "python2026"])
# Retorno Esperado: ["senha1234", "python2026"]
def validar_senhas(lista_senhas:list) -> str:
    senhas_8 = []
    for senha in lista_senhas:
        if len(senha) >= 8:
            senhas_8.append(senha)
    return senhas_8


#Exercício 14: Busca do Primeiro Elemento Fora do Padrão (while)
#Objetivo: Escreva uma função primeiro_impar(numeros) que percorra uma lista usando while e retorne o primeiro número ímpar encontrado. Se não encontrar nenhum, retorne None.
#Exemplo de Chamada: primeiro_impar([2, 4, 6, 9, 10, 11])
#Retorno Esperado: 9
def primeiro_impar(numeros:list) -> int:
    indice = 0
    while indice < len(numeros):
        if numeros[indice] % 2 != 0:
            return numeros[indice]
        indice += 1
    return None


#Exercício 15: Contagem de Frequência de um Elemento
#Objetivo: Escreva uma função contar_ocorrencias(lista, elemento_alvo) que conte quantas vezes elemento_alvo aparece na lista sem utilizar a função .count().
#Exemplo de Chamada: contar_ocorrencias(["a", "b", "a", "c", "a"], "a")
#Retorno Esperado: 3
def contar_ocorrencias(lista:list, elemento_alvo:str):
    letrinhas = 0
    for letra in lista:
        if letra == elemento_alvo:
            letrinhas += 1
    return letrinhas

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
    saque = simular_saque(200,[50, 100, 80, 30])
    print(f'10 - {saque}')
    duplicado = remover_duplicados([1,3,2,3,1,4,2])
    print(f'11 - {duplicado}')
    positivos = media_positivos([-5, 10, -2, 20, 30])
    print(f'12 - {positivos}')
    senhas = validar_senhas(["12345", "senha1234", "admin", "python2026"])
    print(f'13 - {senhas}')
    pega_impar = primeiro_impar([2, 4, 6, 9, 10, 11])
    print(f'14 - {pega_impar}')
    ocorrencias = contar_ocorrencias(["a", "b", "a", "c", "a"],'a')
    print(f'15 - {ocorrencias}')
