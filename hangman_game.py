paises_forca = {
    'BRASIL': 'Copa do Mundo de 2002',
    'FRANÇA': 'Copa do Mundo de 1998',
    'ESPANHA': 'Copa do Mundo de 2010'
}

frutas_forca = {
    'BANANA': 'Fruta amarela',
    'MAÇÃ': 'Fruta vermelha',
    'UVA': 'Fruta roxa'
}

objetos_forca = {
    'CADEIRA': 'Objeto para sentar',
    'CAMA': 'Objeto para dormir',
    'GELADEIRA': 'Objeto para armazenar alimentos'
}

carros_forca = {
    'FUSCA': 'Carro popular',
    'FERRARI': 'Carro esportivo',
    'CAMARO': 'Carro americano'
}

print('[1] PAÍSES\n[2] FRUTAS\n[3] OBJETOS\n[4] CARROS\n[0] SAIR\n')

escolha_tema = int(input('Diante às opções, escolha um tema: '))

while escolha_tema != 0:

    if escolha_tema == 0:
        print('Obrigado por jogar! Até a próxima.')
        break

    if escolha_tema == 1:
        print('')
        print(paises_forca.keys())
        
        escolha_palavra = input('\nEscolha uma palavra: ').strip().upper() # remove espaços em branco e deixa em maiúsculo
        
        if escolha_palavra in paises_forca:
            print('\nDica:', paises_forca[escolha_palavra])

            estado_palavra = ['_' for _ in escolha_palavra]

            tentativas = 6 # braços, pernas, cabeça, tronco

            for i in range(tentativas): 
                print('\nO boneco se inicia vazio e com', i, 'tentativas.\n')    

                print('Palavra:', ' '.join(estado_palavra))
                
                palavra_usuario = input('\nDigite uma letra: ').upper().split()[0] # pega o primeiro caractere da string
                
                if palavra_usuario in escolha_palavra:
                    for index, letra in enumerate(escolha_palavra):
                        if letra == palavra_usuario:
                            estado_palavra[index] = palavra_usuario
                            i == 0
                            print('\nO boneco continua vazio e com', i, 'tentativas.\n')
                else:
                    print('\nPalavra não encontrada.')
                    
                    i+=1

                    if i == 1:
                        print('\nO boneco possui cabeça e houve', i, 'tentativa.\n')
                        continue
                    elif i == 2:
                        print('\nO boneco possui cabeça e tronco e houve', i, 'tentativas.\n')
                        continue
                    elif i == 3:
                        print('\nO boneco possui cabeça, tronco e 1 braço e houve', i, 'tentativas.\n')
                        continue
                    elif i == 4:
                        print('\nO boneco possui cabeça, tronco e 2 braços e houve', i, 'tentativas.\n')
                        continue
                    elif i == 5:
                        print('\nO boneco possui cabeça, tronco, 2 braços e 1 perna e houve', i, 'tentativas.\n')
                        continue
                    else:
                        print('\nO boneco possui cabeça, tronco, 2 braços e 2 pernas e houve', i, 'tentativas.\n')
                        print('\nSuas tentativas acabaram! Infelizmente, você não acertou a palavra.\n')
                        break
                
                if '_' not in estado_palavra:
                    print('Parabéns! Você acertou a palavra.')
                    break
            else:
                print('Infelizmente, você não acertou a palavra.')
                break
        else:
            print('\nPalavra não encontrada.')
            continue
            
    print('[1] PAÍSES\n[2] FRUTAS\n[3] OBJETOS\n[4] CARROS\n[0] SAIR\n')

    escolha_tema = int(input('Diante às opções, escolha um tema: '))