from emprestimo import Cliente, Emprestimo
import pytest


def test_cliente_novo_leva_3():
    cliente = Cliente('Teo', 0)
    emprestimo = Emprestimo(cliente)
    assert emprestimo.limite_emprestimo() == 3


def test_cliente_com_10_emprestimos_leva_3():
    emprestimo = Emprestimo(Cliente("Julia", 10))
    assert emprestimo.limite_emprestimo() == 3

def test_cliente_fiel_com_onze_emprestimos_leva_quatro():
    cliente = Cliente("Beatriz", 11)
    emprestimo = Emprestimo(cliente)
    assert emprestimo.limite_emprestimo() == 4

def test_cliente_fiel_nao_ultrapasa_quatro_jogo():
    cliente = Cliente('Beatriz', 15)
    emprestimo = Emprestimo(cliente)
    emprestimo.adicionar("Jogo1")
    emprestimo.adicionar("Jogo2")
    emprestimo.adicionar("Jogo3")
    emprestimo.adicionar("Jogo4")

    with pytest.raises(ValueError):
        emprestimo.adicionar("Jogo5")

def test_cliente_fel_nao_pega_jogo_repetido():
    cliente = Cliente("Beatriz", 12)
    emprestimo = Emprestimo(cliente)
    emprestimo.adicionar("Zelda")

    with pytest.raises(ValueError):
        emprestimo.adicionar("Zelda")