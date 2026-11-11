from unittest.mock import Mock
from datetime import date
from cobranca import CobradorDeAtrasos, Emprestimo, AvisadorPorWhatsApp

def obter_sabado():
    return date(2026, 11, 7)

def obter_segunda():
    return date(2026, 11, 9)

def test_fim_de_semana_nao_cobra():
    repositorio = Mock()
    avisador = Mock(spec=AvisadorPorWhatsApp)
    
    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio=obter_sabado)
    cobrador.cobrar()
    
    repositorio.abertos.assert_not_called()

def test_atrasado_e_avisado():
    atrasado = Emprestimo(1, "Ana", "51999990001", date(2026, 11, 1))
    
    repositorio = Mock()
    repositorio.abertos.return_value = [atrasado]
    avisador = Mock(spec=AvisadorPorWhatsApp)
    
    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio=obter_segunda)
    cobrador.cobrar()
    
    avisador.avisa.assert_called_once_with(atrasado)
    repositorio.atualiza.assert_called_once_with(atrasado)
    assert cobrador.total_avisados == 1

def test_whatsapp_cai_nao_atualiza_banco_e_guarda_falha():
    atrasado = Emprestimo(1, "Ana", "51999990001", date(2026, 11, 1))
    
    repositorio = Mock()
    repositorio.abertos.return_value = [atrasado]
    
    avisador = Mock(spec=AvisadorPorWhatsApp)
    avisador.avisa.side_effect = ConnectionError("WhatsApp fora do ar")
    
    cobrador = CobradorDeAtrasos(repositorio, avisador, relogio=obter_segunda)
    cobrador.cobrar()
    
    repositorio.atualiza.assert_not_called()
    assert atrasado in cobrador.falhas
    assert cobrador.total_avisados == 0