from uc3.tests_confeitaria1.confeitaria1 import (
    atualizar_cliente,
    criar_cliente,
    deletar_cliente,
    ler_clientes,
)


def test_criar_e_ler_cliente(conexao):
    cliente = criar_cliente(
        conexao,
        "Ana Clara",
        "Rua das Flores",
        100,
        "Centro",
        "Porto Alegre",
        "90010-000",
    )
    assert cliente is not None
    assert cliente.id_cliente is not None

    clientes = ler_clientes(conexao)
    assert len(clientes) == 1
    assert clientes[0][0] == cliente.id_cliente


def test_atualizar_cliente(conexao):
    cliente = criar_cliente(
        conexao,
        "Bruno Silva",
        "Av. Brasil",
        200,
        "Floresta",
        "Porto Alegre",
        "90230-060",
    )
    atualizado = atualizar_cliente(
        conexao,
        cliente.id_cliente,
        "Av. Ipiranga",
        500,
        "Partenon",
        "Porto Alegre",
        "90610-001",
    )
    assert atualizado is True

    clientes = ler_clientes(conexao)
    assert clientes[0][2] == "Av. Ipiranga"
    assert clientes[0][3] == 500


def test_deletar_cliente(conexao):
    cliente = criar_cliente(
        conexao,
        "Carla Souza",
        "Rua Ramiro Barcelos",
        300,
        "Bom Fim",
        "Porto Alegre",
        "90035-007",
    )
    removido = deletar_cliente(conexao, cliente.id_cliente)
    assert removido is True
    assert ler_clientes(conexao) == []


def test_banco_recusa_dado_invalido(conexao):
    # Exemplo: violação de NOT NULL (nome=None) ou CHECK/UNIQUE conforme seu DDL
    invalido = criar_cliente(
        conexao,
        None,
        "Rua Sem Nome",
        10,
        "Centro",
        "Porto Alegre",
        "90000-000",
    )
    assert invalido is None