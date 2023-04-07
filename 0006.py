#Desafio Sistema bancario

menu = """
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Sair
 => """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = int(input(menu))
    
    if opcao == 1:
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"""
            Depósito: R$ {valor:.2f}\n
            """
            print(f"**Valor R${valor:.2f} depositado com sucesso!**\n")
        else:
            print("Operação falhou! O valor informado é inválido.")
          
    elif opcao == 2:
        valor = float(input("Informe o valor de saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = valor > numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_saques:
            print("Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"""
            Saque: R$ {valor:.2f}\n
            """
            numero_saques += 1
            print(f"**Valor R${valor:.2f} sacado com sucesso!**\n")
        else:
            print("Operação falhou! O valor informado é inválido.")
       
    elif opcao == 3:
        print("""
        ============= EXTRATO =============
            """)
        print("""
         Não foram realizadas movimentações.
        """ if not extrato else extrato)
        print(f"""
            Saldo: R$ {saldo:.2f}
        """)
        print("""
        =============== FIM ===============
            """)
    
    elif opcao == 4:
        break
    else:
        print("Operaçãoinválida, por favor selecione novamete a operação desejada.")
