from src.estoque import (
    adicionar_produto,
    atualizar_estoque,
    verificar_alertas,
    estoque_loja
)


def exibir_menu():
    print("\n" + "="*40)
    print("  SISTEMA DE ESTOQUE - LOJA ELÉTRICA ")
    print("="*40)
    print("1. Cadastrar novo produto")
    print("2. Listar produtos no estoque")
    print("3. Atualizar estoque (Venda/Recebimento)")
    print("4. Verificar alertas de estoque")
    print("5. Sair")
    print("="*40)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            print("\n--- CADASTRAR PRODUTO ---")
            codigo = input("Código: ")
            nome = input("Nome: ")
            qtd_atual = int(input("Quantidade atual: "))
            qtd_minima = int(input("Quantidade mínima para alerta: "))
            custo = float(input("Preço de custo (ex: 12.50): "))
            venda = float(input("Preço de venda (ex: 25.00): "))
            
            mensagem = adicionar_produto(codigo, nome, qtd_atual, qtd_minima, custo, venda)
            print(mensagem)

        elif opcao == '2':
            print("\n--- PRODUTOS NO ESTOQUE ---")
            if len(estoque_loja) == 0:
                print("O estoque está vazio. Cadastre um produto primeiro.")
            else:
                for p in estoque_loja:
                    print(f"[{p['codigo']}] {p['nome']} | Qtd: {p['qtd_atual']} | R$ {p['preco_venda']}")

        elif opcao == '3':
            print("\n--- ATUALIZAR ESTOQUE ---")
            codigo = input("Código do produto: ")
            qtd = int(input("Quantidade (Use '-' para venda, ex: -5): "))
            mensagem = atualizar_estoque(codigo, qtd)
            print(mensagem)

        elif opcao == '4':
            print("\n ALERTAS DE ESTOQUE ")
            alertas = verificar_alertas()
            if len(alertas) == 0:
                print("Tudo certo! Nenhum alerta no momento.")
            else:
                for alerta in alertas:
                    print(alerta)

        elif opcao == '5':
            print("\nSaindo do sistema... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()