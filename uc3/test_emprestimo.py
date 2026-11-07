from emprestimo import Cliente, Emprestimo
import pytest

def test_cliente_novo_leva_3():
    cliente = Cliente('Teo', 3)
    assert cliente.limite_emprestimo() == 3

def test_cliente_com_10_emprestimos_leva_3():
    emprestimo = Emprestimo(Cliente("Julia", 10))
    assert emprestimo.limite_emprestimo() == 10