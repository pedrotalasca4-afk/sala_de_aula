# conftest.py — o que o pytest prepara antes de cada teste de integração.
#
# Material da UC3, Aula 05. O pytest lê este arquivo sozinho, pelo nome: as
# fixtures daqui ficam disponíveis para todo teste da mesma pasta.
#
# ANTES DE RODAR: troquem a senha abaixo pela do PostgreSQL de vocês, e criem
# no pgAdmin o banco locadora_teste (o passo a passo está nos slides).

import psycopg2 as pg
import pytest

BANCO_DE_TESTE = {
    "host": "localhost",
    "port": 5432,
    "dbname": "locadora_teste",
    "user": "locador_teste",
    "password": "senha_locador"
}

@pytest.fixture
def conexao():
    conexao = pg.connect(**BANCO_DE_TESTE)
    cursor = conexao.cursor()
    cursor.execute("TRUNCATE jogo, plataforma RESTART IDENTITY CASCADE")
    conexao.commit()
    yield conexao
    conexao.close()
