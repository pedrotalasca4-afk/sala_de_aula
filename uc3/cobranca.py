from datetime import date

class Emprestimo:
    id_emprestimo: int
    cliente: str
    telefone: str | None
    data_prevista: date
    data_entregue: date | None
    avisado_em: date | None

    def __init__(
        self,
        id_emprestimo: int,
        cliente: str,
        telefone: str | None,
        data_prevista: date,
        data_entregue: date | None = None,
        avisado_em: date | None = None
        ):
        self.id_emprestimo = id_emprestimo
        self.cliente = cliente
        self.telefone = telefone
        self.data_prevista = data_prevista
        self.data_entregue = data_entregue
        self.avisado_em = avisado_em

    def atrasado_em(self, hoje: date) -> bool:
        return self.data_entregue is None and hoje > self.data_prevista

    def registrar_aviso(self, hoje: date) -> None:
        self.avisado_em = hoje

    def __repr__(self):
        return f"Emprestimo( {self.id_emprestimo} - {self.cliente} - prazo {self.data_prevista} )"


class RepositorioDeEmprestimos:
    def __init__(self):
        import psycopg2
        self.conexao = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )

    def abertos(self) -> list[Emprestimo]:
        with self.conexao.cursor() as cursor:
            cursor.execute(
                "SELECT e.id_emprestimo, c.nome, c.telefone, "
                "       e.data_prevista, e.data_entregue, e.avisado_em "
                "FROM emprestimo e "
                "JOIN cliente c ON c.id_cliente = e.id_cliente "
                "WHERE e.data_entregue IS NULL "
                "ORDER BY e.id_emprestimo"
            )
            return [Emprestimo(*linha) for linha in cursor.fetchall()]

    def atualiza(self, emprestimo: Emprestimo) -> None:
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "UPDATE emprestimo SET avisado_em = %s WHERE id_emprestimo = %s",
                    (emprestimo.avisado_em, emprestimo.id_emprestimo)
                )
            self.conexao.commit()
        except Exception:
            self.conexao.rollback()
            raise


class AvisadorPorWhatsApp:
    def avisa(self, emprestimo: Emprestimo) -> None:
        print(
            f"[WhatsApp para {emprestimo.telefone}] Olá, {emprestimo.cliente}! "
            f"O prazo do empréstimo {emprestimo.id_emprestimo} venceu em "
            f"{emprestimo.data_prevista:%d/%m/%Y}. Passe na locadora para devolver."
        )


class CobradorDeAtrasos:
    def __init__(self, repositorio, avisador, relogio=date.today):
        self.repositorio = repositorio
        self.avisador = avisador
        self.relogio = relogio
        self.total_avisados = 0
        self.falhas = []

    def cobrar(self) -> None:
        hoje = self.relogio()

        if hoje.weekday() >= 5:
            return

        for emprestimo in self.repositorio.abertos():
            if not emprestimo.atrasado_em(hoje):
                continue
            
            try:
                self.avisador.avisa(emprestimo)
            except Exception:
                self.falhas.append(emprestimo)
                continue

            emprestimo.registrar_aviso(hoje)
            self.repositorio.atualiza(emprestimo)
            self.total_avisados += 1


if __name__ == "__main__":
    repositorio=RepositorioDeEmprestimos()
    avisador=AvisadorPorWhatsApp()
    cobrador = CobradorDeAtrasos(repositorio,avisador)
    cobrador.cobrar()
    print(f"{cobrador.total_avisados} cliente(s) avisado(s).")
