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

#Exercicios 3
def somar_maiores_que(numeros:list, limite:list):
    count = limite
    for numero in numeros:
        if numero > limite:
            count

if __name__=='__main__':
    dobrar([1,2,3,4,5])
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6,])
    print(f'1 -{numeros_pares}')
    negativos = contar_negativos([10, -3, 0, -5, 8, -1])
    print(f'2 -{negativos}')