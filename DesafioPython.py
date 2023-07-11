menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
       valor = float(input("Informe o valor do depósito: "))
       if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f} \n"
       else:
          print("Operação falhou! O valor não é informado.")
       print("Deposito")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= limite_saques
        if excedeu_saldo:
           print("Operação falhou! Você não tem saldo insuficiente!")
        elif excedeu_limite:
           print("Operação falhou! O valor excede o limite de saques!")
        elif excedeu_saque:
           print("Operação falhou! Numero máximo de saques excedido!")
        elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f} \n"
           numero_saques += 1
        else: 
           print("Operação falhou de vez! O valor informado é invalido!")
        print("Sacar")
    elif opcao == "e":
       print("\n================ EXTRATO BC =======================")
       print("Não foram realizados movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("======================================================")
       print("Extrato")
    elif opcao == "q":
       break
    else:
       print("Operação Inválido! Seleciona a opção correta!")

      


    