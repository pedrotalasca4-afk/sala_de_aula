from datetime import date
from unittest.mock import Mock
import pytest
from confeitaria import (
    calcular_preco_com_status_entrega,
    calcular_preco_com_desconto_atraso,
    Pedido,
    RepositorioDePedidos,
    EnviadorDeEmail,
    RelogioDoSistema,
    ProcessadorDePedidos,
)


# --- TESTES DA FUNÇÃO DE BÔNUS (TRÊS ESTADOS DE ENTREGA) ---

def test_produto_entregue_no_dia_recebe_dois_por_cento():
    assert calcular_preco_com_status_entrega(100.0, 'no_dia') == 102.0

def test_produto_valor_zero_com_bonus():
    assert calcular_preco_com_status_entrega(0.0, 'no_dia') == 0.0

def test_produto_entregue_antes_do_prazo_nao_recebe_bonus():
    assert calcular_preco_com_status_entrega(200.0, 'antes') == 200.0

def test_produto_entregue_com_atraso_nao_recebe_bonus():
    assert calcular_preco_com_status_entrega(200.0, 'atrasado') == 200.0

def test_recusa_preco_negativo_no_bonus():
    with pytest.raises(ValueError):
        calcular_preco_com_status_entrega(-50.0, 'no_dia')


# --- TESTES DA FUNÇÃO DE DESCONTO POR ATRASO (0,5% POR DIA) ---

def test_desconto_atraso_zero_dias():
    assert calcular_preco_com_desconto_atraso(200.0, 0) == 200.0

def test_desconto_atraso_um_dia():
    assert calcular_preco_com_desconto_atraso(200.0, 1) == 199.0

def test_desconto_atraso_quatro_dias():
    assert calcular_preco_com_desconto_atraso(200.0, 4) == 196.0

def test_recusa_dias_atraso_negativos():
    with pytest.raises(ValueError):
        calcular_preco_com_desconto_atraso(200.0, -1)


# --- TESTES DO PROCESSADOR DE PEDIDOS (MOCKS) ---

def test_pedido_atrasado_envia_email_de_aviso():
    pedido_atrasado = Pedido(
        id_pedido=1,
        cliente_email="cliente@email.com",
        data_prevista=date(2026, 11, 10)
    )
    repositorio = Mock(spec=RepositorioDePedidos)
    repositorio.buscar_pendentes.return_value = [pedido_atrasado]
    enviador_email = Mock(spec=EnviadorDeEmail)
    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 15)

    processador = ProcessadorDePedidos(repositorio, enviador_email, relogio)
    processador.processar_atrasados()

    assert processador.total_notificados == 1
    enviador_email.enviar.assert_called_once_with(
        "cliente@email.com",
        "O seu pedido #1 está atrasado!"
    )


def test_pedido_no_prazo_nao_envia_email():
    pedido_no_prazo = Pedido(
        id_pedido=2,
        cliente_email="cliente@email.com",
        data_prevista=date(2026, 11, 20)
    )
    repositorio = Mock(spec=RepositorioDePedidos)
    repositorio.buscar_pendentes.return_value = [pedido_no_prazo]
    enviador_email = Mock(spec=EnviadorDeEmail)
    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 15)

    processador = ProcessadorDePedidos(repositorio, enviador_email, relogio)
    processador.processar_atrasados()

    assert processador.total_notificados == 0
    enviador_email.enviar.assert_not_called()