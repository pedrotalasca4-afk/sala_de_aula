import pytest
from confeitaria import calcular_preco_com_bonus, calcular_preco_com_desconto_atraso
from unittest.mock import Mock
from datetime import date
from confeitaria import ProcessadorDePedidos


def test_produto_entregue_mesmo_dia_recebe_bonus():
    assert calcular_preco_com_bonus(100.0, True) == 110.0

def test_produto_valor_zero_com_bonus():
    assert calcular_preco_com_bonus(0.0, True) == 0.0

def test_produto_sem_mesma_data_nao_recebe_bonus():
    assert calcular_preco_com_bonus(200.0, False) == 200.0

def test_recusa_preco_negativo_no_bonus():
    with pytest.raises(ValueError):
        calcular_preco_com_bonus(-50.0, True)


def test_desconto_atraso_zero_dias():
    assert calcular_preco_com_desconto_atraso(200.0, 0) == 200.0

def test_desconto_atraso_um_dia():
    assert calcular_preco_com_desconto_atraso(200.0, 1) == 199.0

def test_desconto_atraso_quatro_dias():
    assert calcular_preco_com_desconto_atraso(200.0, 4) == 196.0

def test_recusa_dias_atraso_negativos():
    with pytest.raises(ValueError):
        calcular_preco_com_desconto_atraso(200.0, -1)



class PedidoFalso:
    def __init__(self, id_pedido, cliente_email, data_prevista, data_entregue=None):
        self.id_pedido = id_pedido
        self.cliente_email = cliente_email
        self.data_prevista = data_prevista
        self.data_entregue = data_entregue

def obter_data_atual():
    return date(2026, 11, 15)

def test_pedido_atrasado_envia_email_de_aviso():
    pedido_atrasado = PedidoFalso(
        id_pedido=1,
        cliente_email="cliente.com",
        data_prevista=date(2026, 11, 10)
    )
    repositorio = Mock()
    repositorio.buscar_pendentes.return_value = [pedido_atrasado]
    enviador_email = Mock()
    processador = ProcessadorDePedidos(repositorio, enviador_email, relogio=obter_data_atual)
    processador.processar_atrasados()
    enviador_email.enviar.assert_called_once_with(
        "cliente.com",
        "O seu pedido #1 está atrasado!"
    )
    assert processador.total_notificados == 1

def test_pedido_no_prazo_nao_envia_email():
    pedido_no_prazo = PedidoFalso(
        id_pedido=2,
        cliente_email="cliente.com",
        data_prevista=date(2026, 11, 20)
    )
    repositorio = Mock()
    repositorio.buscar_pendentes.return_value = [pedido_no_prazo]
    enviador_email = Mock()
    processador = ProcessadorDePedidos(repositorio, enviador_email, relogio=obter_data_atual)
    processador.processar_atrasados()
    enviador_email.enviar.assert_not_called()
    assert processador.total_notificados == 0