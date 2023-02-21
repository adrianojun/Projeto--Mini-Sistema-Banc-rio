# DESAFIO SISTEMA BANCÁRIO: DIO

menu = """"
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else: print("A operação falhou, tente novamente")


    elif opcao == "s":

        valor = float(input("Digite o valor a ser sacado: R$"))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Inválida: Saldo insulficiente!")
        
        elif excedeu_limite:
            print("Operação Inválida: O saque só pode ser efetuado até R$500,00")

        elif excedeu_saque:
            print("Operação Inválida: Você atingiu o limite de saques diários!")
        
        elif valor > 0:
            saldo -= valor
            extrato = f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else: print("Erro, valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("\n Não foram realizadas nenhuma operação." if not extrato else extrato)
        print(f"\nSaldo = R${saldo:.2f}")
        print("\n=========================================")

    elif opcao == "q":
         break

    else: print("Operação inválida, selecione novamente a opção que você deseja.")








        
