class ContaBancaria:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.saldo = 0
        self.registro_transferencias = []

    def deposito(self):
        valor = float(input("\nEnter the amount to be deposited: "))
        self.saldo += valor
        print("\nDeposit successful!\n")
        print(f"Saldo atual: {self.saldo}")

    def saque(self):
        valor = float(input("\nEnter the amount to be withdrawn: "))
        if self.saldo >= valor:
            self.saldo -= valor
            print("\nWithdrawal successful!\n")
        else:
            print("\nInsufficient balance!\n")
        print(f"Saldo atual: {self.saldo}")

    def transferencia(self, destinatario):
        valor = float(input("\nEnter the amount to be transferred: "))
        if self.saldo >= valor:
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

    def consulta_extrato(self):
        print(f"\nYour balance is R$ {self.saldo:.2f}")
        print("\nHistory of your transactions:", self.registro_transferencias)

usuarios = {}

while True:
    print("\n[1] LOGIN\n[2] REGISTER\n[8] EXIT")
    opcao = int(input("\nChoose an option: "))

    if opcao == 1:
        login = input("\nEnter your username: ")
        senha = input("Enter your password: ")

        if login in usuarios and usuarios[login].senha == senha:
            print("\nLogin successful!\n")
            conta = usuarios[login]

            while True:
                print("\n[3] DEPÓSITO\n[4] SAQUE\n[5] TRANSFERÊNCIA DE CONTA\n[6] CONSULTA DE EXTRATO\n[7] VOLTAR")
                opcao = int(input("\nChoose an option: "))

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