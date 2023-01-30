saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[0] Sair


=> """

usuarios = {
    
}

contas = {

}

n_de_contas = 0000

def saque(*, valor):
    global LIMITE_SAQUES
    global numero_saques
    global saldo
    global extrato

    if valor > saldo:
        print("Saldo insuficiente.")
    else:
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques alcançado.")
        elif valor > 500:
            print("O valor máximo permitido é de R$ 500.00 por saque.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f} \n"
            print("Operação bem-sucedida!")

def deposito(valor, /):
    global saldo
    global extrato

    if valor <= 0:
       print("Valor inválido.") 
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} \n"
        print("Operação bem-sucedida!")

def extrato_func():
    global extrato
    global saldo
    print("========== EXTRATO ========== \n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(nome, nascimento, cpf, logradouro):
    
    if cpf in usuarios:
        print("CPF já existente.")
    else:
        usuarios[cpf] = {"nome": nome, "nascimento": nascimento, "logradouro": logradouro}
        print("Usuário criado!")
        print(usuarios)

def criar_conta(cpf, nome):
    global n_de_contas
    if cpf in usuarios:
        n_de_contas += 1
        usuarios[cpf]["Cc"] = f"{n_de_contas}"
        contas[f"{n_de_contas}"] = {"nome": nome, "agencia": "0001"}
        print("Conta vinculada!")
    else:
        n_de_contas += 1
        contas[f"{n_de_contas}"] = {"nome": nome, "agencia": "0001"}
        print("Conta Criada!")
    print(usuarios)
    print(contas)


while True:
    opcao = input(menu)
    

    if opcao == "1":
        print("Depósito")
        deposito(float(input("Digite o valor que deseja depositar: ")))     
    elif opcao == "2":
        print("Saque")
        saque(valor = int(input("Insira o valor desejado: ")))             
    elif opcao == "3":
        extrato_func()
    elif opcao == "4":
        criar_usuario(nome = input("Digite seu nome completo: "), nascimento = input("Digite sua data de nascimento: "), cpf = input("Digite seu CPF: "), logradouro = input("Digite seu logradouro: ") )
    elif opcao == "5":
        criar_conta(cpf = input("Digite o seu CPF: "), nome= input("Digite o seu nome: "))    
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada.")