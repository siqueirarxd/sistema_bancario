saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

while True:
    opcao = input(menu)
    

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Insira o valor que deseja depositar: "))
        if deposito <= 0:
            print("Valor inválido.")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f} \n"
            print("Operação bem-sucedida!")     
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Insira o valor desejado: "))
        if valor_saque > saldo:
            print("Saldo insuficiente.")
        else:
            if numero_saques == LIMITE_SAQUES:
                print("Limite de saques alcançado.")
            elif valor_saque > 500:
                print("O valor máximo permitido é de R$ 500.00 por saque.")
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f} \n"
                print("Operação bem-sucedida!")             
    elif opcao == "e":
        print("========== EXTRATO ========== \n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada.")