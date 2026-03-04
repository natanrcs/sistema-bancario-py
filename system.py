saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")

def sacar(valor):
    global saldo, numero_saques

    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite_saque:
        print("Valor excede o limite por saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R${valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido.")

def mostrar_extrato():
    print("----:::EXTRATO:::----")
    if not extrato:
        print("Nenhuma movimentação.")
    else:
        for mov in extrato:
            print(mov)

    print(f"Saldo atual: r$:{saldo:.2f}")
    print("----::Extrato:::----")
while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input("Insira um numero:"))

    if opcao == 1:
        valor = float(input("Valor do depósito: "))
        depositar(valor)

    elif opcao == 2:
        valor = float(input("Valor do saque: "))
        sacar(valor)

    elif opcao == 3:
        mostrar_extrato()

    elif opcao == 4:
        print("Encerrando sistema bancário...")
        break

    else:
        print("Opção inválida.")