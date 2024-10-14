def deposito():
    valor = float(input("\nEnter the amount to be deposited: "))
    usuarios[login]['saldo'] += valor
    print("\nDeposit successful!\n")
    print(usuarios)
   
def saque():
    valor = float(input("\nEnter the amount to be withdrawn: "))
    
    if usuarios[login]['saldo'] >= valor:
        usuarios[login]['saldo'] -= valor
        print("\nWithdrawal successful!\n")
        print(usuarios)
    else:
        print("\nInsufficient balance!\n")   

def transferencia():
    valor = float(input("\nEnter the amount to be transfer: "))
    
    if usuarios[login]['saldo'] >= valor:
        user_transfer = input("\nEnter the username to transfer: ")
        senha = input("Enter the password: ")
        
        if user_transfer in usuarios and usuarios[user_transfer]['senha'] == senha:
            usuarios[login]['saldo'] -= valor
            usuarios[user_transfer]['saldo'] += valor
            print("\nTransfer successful!\n")
            registro_transferencias.append((valor, user_transfer))
            print(usuarios)
            
        elif user_transfer not in usuarios:
            print("\nUser not found!\n")
            
        else:
            print("\nWrong password!\n")
            
    else:
        print("\nInsufficient balance!\n")
 
def consulta_extrato():
    print("\nYour balance is R$ %.2f" % usuarios[login]['saldo']) # insere o valor do saldo do usuário dentro da string formatada
    print("\nHistory of your transactions: ", registro_transferencias)
 
usuarios = {} # de início, o dicionário de usuários / senha está vazio
registro_transferencias = []
saldo = 0
opcao = 0

while opcao != 8:
    
    print("\n[1] LOGIN\n[2] REGISTER\n[8] EXIT")

    opcao = int(input("\nChoose an option: "))
    
    if opcao == 1:
        login = input("\nEnter your username: ")
        senha = input("Enter your password: ")
        
        if login in usuarios and usuarios[login]['senha'] == senha:
            print("\nLogin successful!\n")
            
            while True:
                print("\n[3] DEPÓSITO\n[4] SAQUE\n[5] TRANSFERÊNCIA DE CONTA\n[6] CONSULTA DE EXTRATO\n[7] VOLTAR")
                opcao = int(input("\nChoose an option: "))            
                
                print(usuarios)
                
                if opcao == 3:
                    deposito()
                
                elif opcao == 4:
                    saque()
                
                elif opcao == 5:
                    transferencia()          
                                    
                elif opcao == 6:
                    consulta_extrato()
                
                elif opcao == 7:
                    print("\nReturning to the main menu...")
                    break
                
        else:
            print("\nLogin or password failed!\n")
            continue 
         
    elif opcao == 2:
        login = input("\nEnter a username: ")
    
        if login in usuarios.keys():
            print("\nThis user is already registered!\n")
            continue
            
        else:
            senha = input("Enter a password: ")
            usuarios[login] = {'senha': senha, 'saldo': 0}
            print("\nUser registered successfully!\n")
            
            print(usuarios)
    
    elif opcao == 8:
        print("\nExiting...")
        break