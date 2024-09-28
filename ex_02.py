usuarios = {
    'ana': ['1234', 15000],
    'julia': ['5678', 14000],
    'luiza': ['9012', 13000],
    'maria': ['3456', 12000]
}

print("[1] LOGIN\n[2] REGISTER\n[3] EXIT")

opcao = int(input("Choose an option: "))

if opcao == 1:
       
    login = input("Enter your username: ")
    senha = input("Enter your password: ")   
       
    while login != usuarios.keys() or senha != usuarios[usuarios.keys()][0]:
    
        login = input("Enter your username: ")
        senha = input("Enter your password: ")
        
        if login == usuarios.keys() and senha == usuarios[usuarios.keys()][0]:
            print("You are logged in.")
            
        print("Invalid username or password.")
            
elif opcao == 2:
    
    login = input("Enter a username: ")
    
    while login == usuarios.keys():
        print("This username is already in use.")
        login = input("Enter a username: ")
        
    senha = input("Enter a password: ")
    
    usuarios[login] = [senha, 10000]
    
    print("You have successfully registered.")            