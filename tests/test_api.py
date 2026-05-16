# tests/test_api.py
from src.api import obter_cotacao_dolar

def test_obter_cotacao_dolar_integracao():
    """Teste de integração real: verifica se a API está online e retorna um float"""
    cotacao = obter_cotacao_dolar()
    
    # Se houver internet, a cotação não pode ser vazia e deve ser um número maior que zero
    assert cotacao is not None
    assert isinstance(cotacao, float)
    assert cotacao > 0.0