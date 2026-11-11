import pytest
from confeitaria import calcular_preco_com_bonus

def test_produto_entrgue_com_atrso_sem_bonus():
    assert calcular_preco_com_bonus(100.0, False) == 100.0

def test_produto_valor_zero():
    assert calcular_preco_com_bonus(0.0, True) == 0.0

def test_produto_entregue_recebe_bonus():
    assert calcular_preco_com_bonus(100.0, True) == 102.0

def test_produto_entregue_antes_do_prazo_nao_recebe_bonus():
    assert calcular_preco_com_bonus(200.0, False) == 200.0

def test_recusa_preco_negativo():
    with pytest.raises(ValueError):
        calcular_preco_com_bonus(-50.0,True)