from relatorio import Aluguel, total_do_cliente
def test_todos_alugueis_mesmo_cliente():
    #Cenário
    alugueis = [
        Aluguel ("Ana","Fifa", 20),
        Aluguel ("Ana", "Skyrim", 30),
        Aluguel ("Ana", "GTA", 10)
    ]
    #Ação
    total = total_do_cliente(alugueis=alugueis,cliente="Ana")
    # Validação
    assert total == 60

def test_soma_todos_alugueis_mais_clientes():
    alugueis = [
        Aluguel ("Ana", "Fifa", 20),
        Aluguel ("Ana", "Skyrim", 30),
        Aluguel ("Carla", "Mario", 50),
        Aluguel ("Carla","Fallout",60),
        Aluguel ("Carla","Half-Life",40),
        Aluguel ("Bruno","Baldur Gate", 30),
        Aluguel ("Bruno", "Sonic", 40),
        Aluguel ("Bruno","God of War",20)
    ]

    total = total_do_cliente(alugueis=alugueis,cliente="Ana")
    assert total == 50

def test_soma_todos_alugueis_mais_clientes_e_adiciona_um():
    alugueis = [
        Aluguel ("Ana", "Fifa", 20),
        Aluguel ("Ana", "Skyrim", 30),
        Aluguel ("Carla", "Mario", 50),
        Aluguel ("Carla","Fallout",60),
        Aluguel ("Carla","Half-Life",40),
        Aluguel ("Bruno","Baldur Gate", 30),
        Aluguel ("Bruno", "Sonic", 40),
        Aluguel ("Bruno","God of War",20)
    ]

    total = total_do_cliente(alugueis=alugueis,cliente="Ana")
    assert total == 50
    alugueis.append(Aluguel("Ana","JOGO1",60))
    total = total_do_cliente(alugueis=alugueis,cliente="Ana")
    assert total == 110
