import pytest
from multa import multa, valor_do_aluguel
def test_multa_antes_de_3_dia():
    assert multa(0) == 0.0
    assert multa(1) == 0.0
    assert multa(2) == 0.0

def test_multa_no_3_dia():
    assert multa(3) == 15.0

def test_multa_depois_3_dia():
    assert multa(4) == 20.0

def test_alugou_por_dias_valido():
    assert valor_do_aluguel(10.0,1) == 10.0

def test_valor_por_dia_negativo_ou_zero_dias():
    if not valor_do_aluguel:
        with pytest.raises(ValueError):
            valor_do_aluguel(5.0,0)