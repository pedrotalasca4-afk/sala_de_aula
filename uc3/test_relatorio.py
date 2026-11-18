from relatorio import Aluguel, total_do_cliente
from confeitaria import calcular_preco_com_status_entrega


def test_cliente_sem_alugueis():
    alugueis = [
        Aluguel("Bruno", "Zelda", 40.0),
        Aluguel("Carla", "Mario Kart", 25.0)
    ]
    assert total_do_cliente(alugueis=alugueis, cliente="Ana") == 0.0


def test_cliente_com_um_unico_aluguel():
    alugueis = [
        Aluguel("Ana", "Fifa", 30.0),
        Aluguel("Bruno", "Zelda", 40.0)
    ]
    assert total_do_cliente(alugueis=alugueis, cliente="Ana") == 30.0


def test_todos_alugueis_mesmo_cliente():
    alugueis = [
        Aluguel("Ana", "Fifa", 20.0),
        Aluguel("Ana", "Skyrim", 30.0),
        Aluguel("Ana", "GTA", 10.0)
    ]
    total = total_do_cliente(alugueis=alugueis, cliente="Ana")
    assert total == 60.0


def test_soma_todos_alugueis_mais_clientes():
    alugueis = [
        Aluguel("Ana", "Fifa", 20.0),
        Aluguel("Ana", "Skyrim", 30.0),
        Aluguel("Carla", "Mario", 50.0),
        Aluguel("Carla", "Fallout", 60.0),
        Aluguel("Carla", "Half-Life", 40.0),
        Aluguel("Bruno", "Baldur Gate", 30.0),
        Aluguel("Bruno", "Sonic", 40.0),
        Aluguel("Bruno", "God of War", 20.0)
    ]
    total = total_do_cliente(alugueis=alugueis, cliente="Ana")
    assert total == 50.0


def test_soma_todos_alugueis_mais_clientes_e_adiciona_um():
    alugueis = [
        Aluguel("Ana", "Fifa", 20.0),
        Aluguel("Ana", "Skyrim", 30.0),
        Aluguel("Carla", "Mario", 50.0),
        Aluguel("Bruno", "Sonic", 40.0)
    ]
    assert total_do_cliente(alugueis=alugueis, cliente="Ana") == 50.0

    alugueis.append(Aluguel("Ana", "JOGO1", 60.0))
    assert total_do_cliente(alugueis=alugueis, cliente="Ana") == 110.0