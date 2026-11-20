import psycopg2 as pg

class Cliente:
    def __init__(
        self,
        nome: str,
        logradouro: str,
        numero: int,
        bairro: str,
        cidade: str,
        cep: str,
        id_cliente: int | None = None,
    ):
        self.id_cliente = id_cliente
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def __str__(self) -> str:
        return (
            f"Cliente(id={self.id_cliente}, nome='{self.nome}', "
            f"endereco='{self.logradouro}, {self.numero} - {self.bairro}, "
            f"{self.cidade} ({self.cep})')"
        )

    def __repr__(self) -> str:
        return self.__str__()


def criar_cliente(
    conexao,
    nome: str,
    logradouro: str,
    numero: int,
    bairro: str,
    cidade: str,
    cep: str,
) -> Cliente | None:
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO cliente (nome, logradouro, numero, bairro, cidade, cep) "
            "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_cliente;",
            (nome, logradouro, numero, bairro, cidade, cep),
        )
        id_cliente = cursor.fetchone()[0]
        conexao.commit()
        return Cliente(nome, logradouro, numero, bairro, cidade, cep, id_cliente=id_cliente)
    except pg.DatabaseError as e:
        print(f"Erro ao criar cliente: {e}")
        conexao.rollback()
        return None


def ler_clientes(conexao) -> list[tuple]:
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM cliente ORDER BY id_cliente;")
        return cursor.fetchall()
    except pg.DatabaseError as e:
        print(f"Erro ao ler clientes: {e}")
        conexao.rollback()
        return []


def atualizar_cliente(
    conexao,
    id_cliente: int,
    novo_logradouro: str,
    novo_numero: int,
    novo_bairro: str,
    nova_cidade: str,
    novo_cep: str,
) -> bool:
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "UPDATE cliente SET logradouro = %s, numero = %s, bairro = %s, "
            "cidade = %s, cep = %s WHERE id_cliente = %s;",
            (novo_logradouro, novo_numero, novo_bairro, nova_cidade, novo_cep, id_cliente),
        )
        conexao.commit()
        return cursor.rowcount > 0
    except pg.DatabaseError as e:
        print(f"Erro ao atualizar cliente: {e}")
        conexao.rollback()
        return False


def deletar_cliente(conexao, id_cliente: int) -> bool:
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s;", (id_cliente,))
        conexao.commit()
        return cursor.rowcount > 0
    except pg.DatabaseError as e:
        print(f"Erro ao deletar cliente: {e}")
        conexao.rollback()
        return False