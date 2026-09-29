#Exercicio 1 (Escreva uma função contar_maiores_de_idade(pessoas) que receba uma lista de tuplas no formato (nome, idade) e retorne a quantidade de pessoas com idade >= 18.)
def contar_maiores_de_idade(pessoas: list):
    contador = 0
    for nome, idade in pessoas:
        if idade >= 18:
            contador += 1
    return contador


#Exercicio 2 ( Escreva uma função calcular_estoque_total(produtos) que receba um dicionário onde a chave é o nome do produto e o valor é a quantidade em estoque. Retorne a soma total de itens.
# Exemplo de Chamada: calcular_estoque_total({"caneta": 10, "caderno": 5, "borracha": 8}))
def calcular_estoque_total(produtos:dict):
    total = sum(estoque.values())
    return total


#Exercicio 3 (Escreva uma função filtrar_aprovados(notas_alunos) que receba um dicionário {nome: nota} e retorne uma lista com o nome dos alunos aprovados (nota >= 7.0).
# Exemplo de Chamada: filtrar_aprovados({"Alice": 8.5, "Bruno": 5.0, "Carla": 7.0}))
def filtrar_aprovados(notas_alunos:dict):
    for aluno in alunos:
        if alunos.values() >= 7:
            return aluno


if __name__ == '__main__':
    pessoas = [("Ana", 17), ("Bruno", 22), ("Carla", 19)]
    resultado_idade = contar_maiores_de_idade(pessoas)
    print(f'1 - {resultado_idade}')
    
    estoque = ({"caneta": 10, "caderno": 5, "borracha": 8})
    resultado_estoque = calcular_estoque_total(estoque)
    print(f'2 - {resultado_estoque}')
    
    alunos = {"Alice": 8.5, "Bruno": 5.0, "Carla": 7.0}
    resultado_alunos = calcular_estoque_total(alunos)
    print(f'3 - {resultado_alunos}')



