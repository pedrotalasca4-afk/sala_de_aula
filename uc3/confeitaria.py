def calcular_preco_com_bonus(preco:float, entrega:bool):
    if preco < 0:
        raise ValueError('Não se aceita preco negativo')
    
    if entrega:
        return preco * 1.02
    return preco

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
                    f"seu pedido #{pedido.id_pedido} esta atrasado"
                )
                self.total_notificados += 1