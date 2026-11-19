from decimal import Decimal
from crud_jogo import (criar_jogo,buscar_jogo,buscar_por_titulo,atualizar_preco,deletar_jogo,)

def test_criar_e_buscar_por_id(conexao):
    jogo = criar_jogo(conexao, "Zelda", "Aventura", 2017, Decimal("8.00"))
    assert jogo is not None
    assert jogo.id_jogo is not None

    encontrado = buscar_jogo(conexao, jogo.id_jogo)
    assert encontrado is not None
    assert encontrado.titulo == "Zelda"
    assert encontrado.genero == "Aventura"

def test_buscar_por_titulo(conexao):
    criar_jogo(conexao, "Mario Kart", "Corrida", 2017, Decimal("10.00"))
    encontrado = buscar_por_titulo(conexao, "Mario Kart")
    assert encontrado is not None
    assert encontrado.titulo == "Mario Kart"

def test_atualizar_preco(conexao):
    jogo = criar_jogo(conexao, "God of War", "Ação", 2018, Decimal("12.00"))
    sucesso = atualizar_preco(conexao, jogo.id_jogo, Decimal("15.00"))
    assert sucesso is True

    atualizado = buscar_jogo(conexao, jogo.id_jogo)
    assert atualizado.preco_diaria == Decimal("15.00")

def test_deletar_jogo(conexao):
    jogo = criar_jogo(conexao, "Elden Ring", "RPG", 2022, Decimal("18.00"))
    sucesso = deletar_jogo(conexao, jogo.id_jogo)
    assert sucesso is True

    removido = buscar_jogo(conexao, jogo.id_jogo)
    assert removido is None

def test_deletar_jogo_com_plataforma(conexao):
    jogo = criar_jogo(conexao, "Switch Game", "Aventura", 2021, Decimal("14.00"))
    
    # Vinculando a uma plataforma para testar restrição de chave estrangeira
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO plataforma (nome) VALUES ('Nintendo Switch') RETURNING id_plataforma")
    id_plat = cursor.fetchone()[0]
    cursor.execute("INSERT INTO jogos_plataforma (id_jogo, id_plataforma) VALUES (%s, %s)", (jogo.id_jogo, id_plat))
    conexao.commit()

    sucesso = deletar_jogo(conexao, jogo.id_jogo)
    assert isinstance(sucesso, bool)

def test_banco_recusa_preco_negativo(conexao):
    # Violação da constraint CHECK do banco (preço >= 0)
    resultado = criar_jogo(conexao, "Invalido", "Ação", 2020, Decimal("-5.00"))
    assert resultado is None

def test_banco_recusa_titulo_repetido(conexao):
    criar_jogo(conexao, "Unico", "Ação", 2020, Decimal("10.00"))
    # Violação da constraint UNIQUE no título
    resultado = criar_jogo(conexao, "Unico", "RPG", 2021, Decimal("12.00"))
    assert resultado is None