# 📦 Controle de Estoque - Loja de Elétrica

## 🎯 Sobre o Projeto
Este projeto é uma aplicação de linha de comando (CLI) desenvolvida para resolver um problema real de desorganização e falta de controle de estoque em lojas de materiais elétricos e de construção. 

## 🚨 O Problema (Dor Real)
Muitas lojas do setor elétrico operam com sistemas antigos ou sem nenhum controle digital, resultando em:
* Perda de vendas por falta de produtos na prateleira.
* Dificuldade de saber a hora exata de repor o estoque.
* Trabalho braçal excessivo para conferência.

## 💡 A Solução
Um sistema simples e direto que permite o cadastro de produtos elétricos (como painéis de LED, fios, disjuntores) e emite alertas automáticos quando um item atinge a quantidade mínima, facilitando o pedido junto aos fornecedores.

## 👥 Público-Alvo
* Donos de pequenas lojas de materiais elétricos.
* Gerentes de estoque.
* Atendentes e vendedores.

## ⚙️ Funcionalidades Principais
* Cadastro de novos produtos.
* Atualização de quantidade (entrada e saída).
* Alerta automático de estoque baixo.
* Alerta de produto em falta (estoque zero).

## 🛠️ Tecnologias Utilizadas
* Python 3
* Pytest (Testes automatizados)
* Flake8 (Linting/Análise Estática)
* GitHub Actions (CI/CD)

## 🕹️ Como Usar o Sistema (Passo a Passo)

Após iniciar o programa com o comando `python main.py`, você verá um menu interativo. Veja um exemplo de fluxo de uso de ponta a ponta:

1. **Cadastrar um Produto (Opção 1):**
   - Digite `1` e pressione Enter.
   - Preencha os dados solicitados pelo sistema. 
   - *Exemplo:* Código: `001`, Nome: `Lâmpada LED 9W`, Qtd atual: `50`, Qtd mínima: `10`, Custo: `5.00`, Venda: `12.00`.

2. **Verificar o Estoque (Opção 2):**
   - Digite `2` e pressione Enter.
   - O sistema listará todos os produtos cadastrados, mostrando a quantidade atual e o preço de venda.

3. **Registrar uma Venda ou Recebimento (Opção 3):**
   - Digite `3` e pressione Enter.
   - Informe o código do produto (ex: `001`).
   - Para registrar uma **venda**, digite um valor negativo (ex: `-5` para subtrair 5 unidades).
   - Para registrar um **recebimento** do fornecedor, digite um valor positivo (ex: `20` para somar 20 unidades).

4. **Consultar Alertas de Reposição (Opção 4):**
   - Digite `4` e pressione Enter.
   - O sistema fará uma varredura e avisará automaticamente se algum produto estiver com o estoque abaixo do mínimo estabelecido ou totalmente esgotado.

5. **Encerrar o Programa (Opção 5):**
   - Digite `5` para sair do sistema de forma segura.

   ## 🚀 Como Baixar e Executar o Projeto na Sua Máquina

Se você quiser testar este projeto no seu próprio computador, siga o passo a passo abaixo. 

### Pré-requisitos
Você precisará ter instalado na sua máquina:
- **Python** (versão 3.10 ou superior)
- **Git** (para clonar o repositório)

### Instalação Passo a Passo

1. **Clone o repositório:**
   Abra o seu terminal e digite o comando abaixo para baixar o código:
   ```bash
   git clone [/https://github.com/Zackzinzz07/estoque_eletrica](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)

   Tutorial:
   https://www.youtube.com/watch?v=5ctmK6fV1NQ