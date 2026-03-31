from src.estoque import (
    adicionar_produto,
    atualizar_estoque,
    verificar_alertas,
    estoque_loja
)


def test_adicionar_produto_sucesso():
    estoque_loja.clear()
    resultado = adicionar_produto(
        "001", "Painel LED 18W", 50, 15, 12.50, 25.00
    )
    assert resultado == "Sucesso: Produto 'Painel LED 18W' cadastrado!"
    assert len(estoque_loja) == 1
    assert estoque_loja[0]["codigo"] == "001"


def test_atualizar_estoque():
    estoque_loja.clear()
    adicionar_produto("002", "Fio 2.5mm", 100, 20, 50.0, 80.0)
    resultado = atualizar_estoque("002", -30)

    assert resultado == "Estoque atualizado. Nova quantidade: 70"
    assert estoque_loja[0]["qtd_atual"] == 70


def test_verificar_alertas():
    estoque_loja.clear()
    adicionar_produto("003", "Disjuntor 20A", 5, 10, 10.0, 20.0)
    adicionar_produto("004", "Fita Isolante", 0, 5, 2.0, 5.0)
    adicionar_produto("005", "Lâmpada LED", 50, 10, 8.0, 15.0)

    alertas = verificar_alertas()

    assert len(alertas) == 2
    assert "Atenção: Disjuntor 20A" in alertas[0]
    assert "ALERTA VERMELHO: Fita Isolante" in alertas[1]