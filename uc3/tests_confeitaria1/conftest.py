# conftest.py — o que o pytest prepara antes de cada teste de integração.
#
# Material da UC3, Aula 05. O pytest lê este arquivo sozinho, pelo nome: as
# fixtures daqui ficam disponíveis para todo teste da mesma pasta.
#
# ANTES DE RODAR: troquem a senha abaixo pela do PostgreSQL de vocês, e criem
# no pgAdmin o banco locadora_teste (o passo a passo está nos slides).

import psycopg2 as pg
import pytest
from uc3.config_local import SENHA

BANCO_DE_TESTE = {
    "host": "localhost",
    "port": 5432,
    "dbname": "confeitaria_teste",
    "user": "atendente_teste",
    "password": SENHA,
}


@pytest.fixture
def conexao():
    conexao = pg.connect(**BANCO_DE_TESTE)
    cursor = conexao.cursor()
    cursor.execute(
        "TRUNCATE solicitacao, item_pedido, pedido, doce, tipo_doce, "
        "cliente_telefone, cliente RESTART IDENTITY CASCADE"
    )
    conexao.commit()
    yield conexao
    conexao.close()