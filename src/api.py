# src/api.py
import requests

def obter_cotacao_dolar():
    """Busca a cotação atual do dólar usando a AwesomeAPI."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Verifica se deu erro (ex: 404)
        dados = response.json()
        
        # Fazemos a conversão e já retornamos direto na mesma linha!
        return float(dados['USDBRL']['bid'])
        
    except (requests.RequestException, KeyError, ValueError):
        return None
    