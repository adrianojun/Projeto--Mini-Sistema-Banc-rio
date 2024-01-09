import textwrap


def menu():
    return f"""
    ============== MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tSair
    """


def depositar(saldo, valor, extrato, /):
    valor = float(input('Digite o valor a ser depositado: R$'))
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}'
        print("Depósito realizado com sucesso!")
    else: print("Operação Inválida!")
        
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numeros_saques, limites_saques):
    valor = float(input("Digite o valor a ser sacado: R$"))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques > limites_saques
    
    if excedeu_saldo:
        print("Operação Inválida: Seu saldo é insulficiente!")
        
    elif excedeu_limite:
        print("Operação Inválida: Saque disponível somente até R$500,00")
    
    elif excedeu_saques:
        print("Operação Inválida: Você excedeu o número de saques diários")
        
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numeros_saques += 1
        print("Saque realizado com sucesso!")
        
    else: print("Valor informado é inválido!!!")
        
    
    
    return saldo, extrato    


def exibir_extrato(saldo, /, *, extrato,):
    print("\n================ EXTRATO ================")
    print("\n Não foram realizadas nenhuma operação." if not extrato else extrato)
    print(f"\nSaldo = R${saldo:.2f}")
    print("\n=========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números:)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (longradouro, numero - bairro, cidade/sigla do estado): ")    
    
    usuarios.append({"Nome": nome, "Data_nascimento": data_nascimento, "CPF":cpf, "Endereço":endereco})
    
    print("=== Usuário cadastrado com sucesso ===")
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados =[usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta_bancaria(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso!!! ===")
        return{"Agência": agencia, "Número da Conta": numero_conta, "Usuário": usuario}
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["Agência"]}
            C/C: \t{conta["Número da Conta"]}
            Titular:\t{conta["Usuario"]["Nome"]}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True: 
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor de saque: R$"))
            
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limites_saques=LIMITE_SAQUES 
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta_bancaria(AGENCIA, numero_conta, usuarios)
            
            if conta:
                conta.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:  
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            

main()
        
        
            