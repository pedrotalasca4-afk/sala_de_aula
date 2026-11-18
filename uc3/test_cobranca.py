from datetime import date
from unittest.mock import Mock
from cobranca import (Emprestimo,RepositorioDeEmprestimos,AvisadorPorWhatsApp,RelogioDoSistema,CobradorDeAtrasos,)

def test_avisa_quem_passou_do_prazo():
    atrasado = Emprestimo(1, "Ana Souza", "51 99999-0001", date(2026, 11, 1))

    repositorio = Mock(spec=RepositorioDeEmprestimos)
    repositorio.abertos.return_value = [atrasado]
    avisador = Mock(spec=AvisadorPorWhatsApp)
    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 10)  # Terça-feira

    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio)
    cobrador.cobrar()

    assert cobrador.total_avisados == 1
    assert atrasado.avisado_em == date(2026, 11, 10)
    avisador.avisa.assert_called_once_with(atrasado)
    repositorio.atualiza.assert_called_once_with(atrasado)

def test_nao_avisa_quem_ainda_esta_no_prazo():
    no_prazo = Emprestimo(2, "Carlos Lima", "51 99999-0002", date(2026, 11, 20))

    repositorio = Mock(spec=RepositorioDeEmprestimos)
    repositorio.abertos.return_value = [no_prazo]
    avisador = Mock(spec=AvisadorPorWhatsApp)
    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 10)

    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio)
    cobrador.cobrar()

    assert cobrador.total_avisados == 0
    avisador.avisa.assert_not_called()
    repositorio.atualiza.assert_not_called()

def test_nao_avisa_no_dia_do_prazo():
    vence_hoje = Emprestimo(3, "Lucas Silva", "51 99999-0003", date(2026, 11, 10))

    repositorio = Mock(spec=RepositorioDeEmprestimos)
    repositorio.abertos.return_value = [vence_hoje]
    avisador = Mock(spec=AvisadorPorWhatsApp)
    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 10)

    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio)
    cobrador.cobrar()

    assert cobrador.total_avisados == 0
    avisador.avisa.assert_not_called()

def test_nao_cobra_no_fim_de_semana():
    atrasado = Emprestimo(4, "Beatriz", "51 99999-0004", date(2026, 11, 1))

    repositorio = Mock(spec=RepositorioDeEmprestimos)
    repositorio.abertos.return_value = [atrasado]
    avisador = Mock(spec=AvisadorPorWhatsApp)
    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 14)  # Sábado

    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio)
    cobrador.cobrar()

    assert cobrador.total_avisados == 0
    avisador.avisa.assert_not_called()

def test_whatsapp_fora_do_ar_nao_para_a_cobranca():
    primeiro = Emprestimo(1, "Ana", "51 99999-0001", date(2026, 11, 1))
    segundo = Emprestimo(2, "Bruno", "51 99999-0002", date(2026, 11, 1))

    repositorio = Mock(spec=RepositorioDeEmprestimos)
    repositorio.abertos.return_value = [primeiro, segundo]

    avisador = Mock(spec=AvisadorPorWhatsApp)
    avisador.avisa.side_effect = [ConnectionError("WhatsApp fora do ar"), None]

    relogio = Mock(spec=RelogioDoSistema)
    relogio.hoje.return_value = date(2026, 11, 10)

    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio)
    cobrador.cobrar()

    assert cobrador.total_avisados == 1
    assert primeiro in cobrador.falhas
    assert primeiro.avisado_em is None
    assert segundo.avisado_em == date(2026, 11, 10)
    repositorio.atualiza.assert_called_once_with(segundo)