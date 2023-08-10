def main():
    saldo = 0
    extrato = []
    
    while True:
        print("Banco Quintanilha")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo += valor
            extrato.append(f"Depósito: + R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            if valor <= saldo:
                saldo -= valor
                extrato.append(f"Saque: - R$ {valor:.2f}")
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque.")
        elif opcao == "3":
            print("\nExtrato:")
            for movimento in extrato:
                print(movimento)
            print(f"Saldo atual: R$ {saldo:.2f}\n")
        elif opcao == "4":
            print("Obrigado por usar nosso sistema. Até logo!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
