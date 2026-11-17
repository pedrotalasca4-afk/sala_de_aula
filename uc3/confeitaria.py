def calcular_preco_com_bonus(preco: float, entrega: bool):
    """Aplica 2% de bônus ao produto entregue na data prevista."""
    if preco < 0:
        raise ValueError('Não se aceita preço negativo')
    if entrega:
        return round(preco * 1.02, 2)
    return preco


def calcular_preco_com_desconto_atraso(preco: float, dias_atraso: int):
    """Aplica desconto de 0,5% por dia de atraso (acumulativo)."""
    if preco < 0:
        raise ValueError('Não se aceita preço negativo')
    if dias_atraso < 0:
        raise ValueError('Dias de atraso não podem ser negativos')
    
    desconto_total = dias_atraso * 0.005
    return round(preco * (1 - desconto_total), 2)


class ProcessadorDePedidos:
    def __init__(self, repositorio_pedidos, enviador_email, relogio):
        self.repositorio_pedidos = repositorio_pedidos
        self.enviador_email = enviador_email
        self.relogio = relogio
        self.total_notificados = 0

    def processar_atrasados(self) -> None:
        hoje = self.relogio()

        for pedido in self.repositorio_pedidos.buscar_pendentes():
            if pedido.data_entregue is None and hoje > pedido.data_prevista:
                self.enviador_email.enviar(
                    pedido.cliente_email,
                    f"O seu pedido #{pedido.id_pedido} está atrasado!"
                )
                self.total_notificados += 1