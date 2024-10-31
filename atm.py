class ContaBancaria:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.saldo = 0
        self.registro_transferencias = []

    def deposito(self):
        try:
            valor = float(input("\nEnter the amount to be deposited: "))
            if valor > 0:
                self.saldo += valor
                print("\nDeposit successful!\n")
            else:
                print("\nThe deposit amount must be greater than zero.\n")
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")
        print(f"Saldo atual: {self.saldo}")

    def saque(self):
        try:
            valor = float(input("\nEnter the amount to be withdrawn: "))
            if valor <= 0:
                print("\nThe withdrawal amount must be greater than zero.\n")
            elif self.saldo >= valor:
                self.saldo -= valor
                print("\nWithdrawal successful!\n")
            else:
                print("\nInsufficient balance!\n")
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")
        print(f"Saldo atual: {self.saldo}")

    def transferencia(self, destinatario):
        try:
            valor = float(input("\nEnter the amount to be transferred: "))
            if valor <= 0:
                print("\nThe transfer amount must be greater than zero.\n")
            elif self.saldo >= valor:
                senha = input("\nEnter your password: ")
                if self.senha == senha:
                    self.saldo -= valor
                    destinatario.saldo += valor
                    self.registro_transferencias.append((valor, destinatario.usuario))
                    print("\nTransfer successful!\n")
                else:
                    print("\nWrong password!\n")
            else:
                print("\nInsufficient balance!\n")
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")

    def consulta_extrato(self):
        print(f"\nYour balance is R$ {self.saldo:.2f}")
        print("\nHistory of your transactions:", self.registro_transferencias)


usuarios = {}

while True:
    print("\n[1] LOGIN\n[2] REGISTER\n[8] EXIT")
    try:
        opcao = int(input("\nChoose an option: "))
    except ValueError:
        print("\nInvalid input! Please enter a valid option.")
        continue

    if opcao == 1:
        login = input("\nEnter your username: ")
        senha = input("Enter your password: ")

        if login in usuarios and usuarios[login].senha == senha:
            print("\nLogin successful!\n")
            conta = usuarios[login]

            while True:
                print("\n[3] DEPÓSITO\n[4] SAQUE\n[5] TRANSFERÊNCIA DE CONTA\n[6] CONSULTA DE EXTRATO\n[7] VOLTAR")
                try:
                    opcao = int(input("\nChoose an option: "))
                except ValueError:
                    print("\nInvalid input! Please enter a valid option.")
                    continue

                if opcao == 3:
                    conta.deposito()

                elif opcao == 4:
                    conta.saque()

                elif opcao == 5:
                    user_transfer = input("\nEnter the username to transfer: ")
                    if user_transfer in usuarios:
                        destinatario = usuarios[user_transfer]
                        conta.transferencia(destinatario)
                    else:
                        print("\nUser not found!\n")

                elif opcao == 6:
                    conta.consulta_extrato()

                elif opcao == 7:
                    break

                else:
                    print("\nInvalid option! Please choose a valid option.")

        else:
            print("\nLogin or password failed!\n")

    elif opcao == 2:
        login = input("\nEnter a username: ")
        if login in usuarios:
            print("\nThis user is already registered!\n")
        else:
            senha = input("Enter a password: ")
            usuarios[login] = ContaBancaria(login, senha)
            print("\nUser registered successfully!\n")

    elif opcao == 8:
        print("\nExiting...")
        break

    else:
        print("\nInvalid option! Please choose a valid option.")
