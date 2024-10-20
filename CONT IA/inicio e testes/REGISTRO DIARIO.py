import pandas as pd

# Criação do DataFrame para o livro diário
livro_diario = pd.DataFrame(
    columns=["Data", "Descrição", "Conta Débito", "Valor Débito", "Conta Crédito", "Valor Crédito"])


# Função para adicionar registros
def adicionar_registro(data, descricao, conta_debito, valor_debito, conta_credito, valor_credito):
    global livro_diario
    novo_registro = {
        "Data": data,
        "Descrição": descricao,
        "Conta Débito": conta_debito,
        "Valor Débito": valor_debito,
        "Conta Crédito": conta_credito,
        "Valor Crédito": valor_credito
    }
    livro_diario = pd.concat([livro_diario, pd.DataFrame([novo_registro])], ignore_index=True)


# Loop para entrada de dados pelo usuário
while True:
    data = input("Digite a data da transação (dd/mm/aaaa): ")
    descricao = input("Digite a descrição da transação: ")
    conta_debito = input("Digite a conta a ser debitada: ")
    valor_debito = float(input("Digite o valor do débito: "))
    conta_credito = input("Digite a conta a ser creditada: ")
    valor_credito = float(input("Digite o valor do crédito: "))

    adicionar_registro(data, descricao, conta_debito, valor_debito, conta_credito, valor_credito)

    mais = input("Deseja adicionar outra transação? (s/n): ")
    if mais.lower() != 's':
        break

print(livro_diario)
