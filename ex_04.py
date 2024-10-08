def cadastro_conta():
    login = input("\nEnter a username: ")
    
    if login in usuarios.keys():
        print("\nThis user is already registered!\n")
        
    else:
        senha = input("Enter a password: ")
        usuarios[login] = {'senha': senha, 'saldo': 0}
        print("\nUser registered successfully!\n")

def login_conta():
    login = input("\nEnter your username: ")
    senha = input("Enter your password: ")
    
    if login in usuarios and usuarios[login]['senha'] == senha:
        print("\nLogin successful!\n")
    else:
        print("\nLogin or password failed!\n")

usuarios = {} # de início, o dicionário de usuários / senha está vazio
saldo = 0

print("[1] LOGIN\n[2] REGISTER\n[7] EXIT")

opcao = int(input("\nChoose an option: "))

while opcao != 7:
    
    if opcao == 1:
        login_conta()   
        
        print("\n[3] DEPÓSITO\n[4] SAQUE\n[5] TRANSFERÊNCIA DE CONTA\n[6] CONSULTA DE EXTRATO")
        
        opcao = int(input("\nChoose an option: "))
        
        if opcao == 3:
            valor = float(input("\nEnter the amount to be deposited: "))
            saldo += valor
            print("\nDeposit successful!\n")
            
        elif opcao == 4:
            valor = float(input("\nEnter the amount to be withdrawn: "))
            
            if saldo >= valor:
                saldo -= valor
                print("\nWithdrawal successful!\n")
            else:
                print("\nInsufficient balance!\n")
        
        elif opcao == 5:
            valor = float(input("\nEnter the amount to be transfer: "))
            
            if saldo >= valor:
                user_transfer = input("\nEnter the username to transfer: ")
                senha = input("Enter the password: ")
                
                if user_transfer in usuarios.keys() and usuarios[user_transfer]['senha'] == senha:
                    usuarios[user_transfer]['saldo'] += valor
                    saldo -= valor
                    print("\nTransfer successful!\n")
                    
                elif user_transfer not in usuarios.keys():
                    print("\nUser not found!\n")
                    
                else:
                    print("\nWrong password!\n")

            else:
                print("\nInsufficient balance!\n")            
                
        elif opcao == 6:
            print("\nSeu saldo é de R$ %.2f", saldo)
            print("Histórico de suas transações:")
            
    elif opcao == 2:
        cadastro_conta()
    
    elif opcao == 7:
        print("\nExiting...")
        break
      
    print(usuarios)
    
    print("\n[1] LOGIN\n[2] REGISTER\n[7] EXIT")

    opcao = int(input("\nChoose an option: "))