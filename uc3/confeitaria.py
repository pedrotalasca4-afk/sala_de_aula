from datetime import date

def calcular_preco_com_status_entrega(preco: float, status_entrega: str):
    """
    Calcula o preço com base nos três estados de entrega:
    - 'antes': entregue antes do prazo (sem bônus)
    - 'no_dia': entregue exatamente na data prevista (recebe 2% de bônus)
    - 'atrasado': entregue com atraso
    """
    if preco < 0:
        raise ValueError('Não se aceita preço negativo')
    
    if status_entrega == 'no_dia':
        return round(preco * 1.02, 2)
    elif status_entrega == 'antes' or status_entrega == 'atrasado':
        return round(preco, 2)
    else:
        raise ValueError('Status de entrega inválido')


def calcular_preco_com_desconto_atraso(preco: float, dias_atraso: int):
    """Aplica desconto de 0,5% por dia de atraso (acumulativo)."""
    if preco < 0:
        raise ValueError('Não se aceita preço negativo')
    if dias_atraso < 0:
        raise ValueError('Dias de atraso não podem ser negativos')
    
    desconto_total = dias_atraso * 0.005
    return round(preco * (1 - desconto_total), 2)


class Pedido:
    def __init__(
        self,
        id_pedido: int,
        cliente_email: str,
        data_prevista: date,
        data_entregue: date | None = None
    ):
        self.id_pedido = id_pedido
        self.cliente_email = cliente_email
        self.data_prevista = data_prevista
        self.data_entregue = data_entregue

    def atrasado_em(self, hoje: date) -> bool:
        return self.data_entregue is None and hoje > self.data_prevista


class RepositorioDePedidos:
    def buscar_pendentes(self) -> list[Pedido]:
        raise NotImplementedError("Conecta no PostgreSQL em produção")


class EnviadorDeEmail:
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-mail para {destinatario}] {mensagem}")


class RelogioDoSistema:
    def hoje(self) -> date:
        return date.today()


class ProcessadorDePedidos:
    def __init__(self, repositorio_pedidos, enviador_email, relogio):
        self.repositorio_pedidos = repositorio_pedidos
        self.enviador_email = enviador_email
        self.relogio = relogio
        self.total_notificados = 0

    def processar_atrasados(self) -> None:
        hoje = self.relogio.hoje()

        for pedido in self.repositorio_pedidos.buscar_pendentes():
            if pedido.atrasado_em(hoje):
                self.enviador_email.enviar(
                    pedido.cliente_email,
                    f"O seu pedido #{pedido.id_pedido} está atrasado!"
                )
                self.total_notificados += 1