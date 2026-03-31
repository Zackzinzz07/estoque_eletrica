estoque_loja = []


def adicionar_produto(codigo, nome, qtd_atual, qtd_minima, custo, venda):
    """Cadastra um novo produto no estoque."""
    for produto in estoque_loja:
        if produto["codigo"] == codigo:
            return f"Erro: Já existe um produto com o código '{codigo}'."

    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "qtd_atual": qtd_atual,
        "qtd_minima": qtd_minima,
        "preco_custo": custo,
        "preco_venda": venda
    }

    estoque_loja.append(novo_produto)
    return f"Sucesso: Produto '{nome}' cadastrado!"


def atualizar_estoque(codigo, quantidade_mudanca):
    """Atualiza a quantidade de um produto."""
    for produto in estoque_loja:
        if produto["codigo"] == codigo:
            produto["qtd_atual"] += quantidade_mudanca
            nova_qtd = produto['qtd_atual']
            return f"Estoque atualizado. Nova quantidade: {nova_qtd}"

    return "Erro: Produto não encontrado."


def verificar_alertas():
    """Retorna avisos para produtos zerados ou abaixo do mínimo."""
    alertas = []
    for produto in estoque_loja:
        if produto["qtd_atual"] == 0:
            nome = produto['nome']
            alertas.append(f"ALERTA VERMELHO: {nome} está ESGOTADO!")
        elif produto["qtd_atual"] <= produto["qtd_minima"]:
            nome = produto['nome']
            qtd = produto['qtd_atual']
            alertas.append(f"Atenção: {nome} com estoque baixo ({qtd} un).")

    return alertas