def jogando_forca():
    erros = 0
    tentativas = 6 # braços, pernas, cabeça, tronco
    letras_digitadas = []
    pontos_segundo_jogador = 0
    pontos_terceiro_jogador = 0

    nome_segundo_jogador = str(input('Digite o nome do 1º jogador: ')).split()[0] # '.split()' divide uma string em uma lista de substrings, com base em um delimitador especificado e, neste caso, pega o primeiro caractere

    opcao_teceiro_jogador = int(input('\n[1] SIM\n[2] NÃO\n\nDeseja adicionar mais de 1 jogador? '))

    if opcao_teceiro_jogador == 1:
        nome_terceiro_jogador = str(input('\nDigite o nome do 2º jogador: ')).split()[0]
        print('\n')

        while erros < tentativas:
            print('\nPalavra:', ' '.join(estado_palavra))

            tentativa_segundo_jogador = input(f'\n{nome_segundo_jogador}, digite uma letra: ').upper().split()[0]

            if tentativa_segundo_jogador in letras_digitadas:
                print('\nEssa letra já está na palavra! Tente outra...\n')
                pontos_segundo_jogador -= 2
                continue

            letras_digitadas.append(tentativa_segundo_jogador)

            if tentativa_segundo_jogador in palavra_terceiro_jogador:
                for index, letra in enumerate(palavra_terceiro_jogador):
                    if letra == tentativa_segundo_jogador:
                        estado_palavra[index] = tentativa_segundo_jogador
                        pontos_segundo_jogador += 10
                print('\nPalavra:', ' '.join(estado_palavra))

                if '_' not in estado_palavra:
                    print('\nA palavra foi completada.')

                    if pontos_segundo_jogador > pontos_terceiro_jogador:
                        print(f'\nParabéns, {nome_segundo_jogador}! Você acertou a palavra.')
                        print(f'\nSegue o ranking:\n\n{nome_terceiro_jogador} - {pontos_terceiro_jogador} pontos\n{nome_segundo_jogador} - {pontos_segundo_jogador} pontos\n')

                    elif pontos_segundo_jogador < pontos_terceiro_jogador:
                        print(f'\nParabéns, {nome_terceiro_jogador}! Você acertou a palavra.')
                        print(f'\nSegue o ranking:\n\n{nome_segundo_jogador} - {pontos_segundo_jogador} pontos\n{nome_terceiro_jogador} - {pontos_terceiro_jogador} pontos\n')

                    else:
                        print('\nHouve um empate! Que curioso! Parabéns para ambos!\n')

                    break

            else:
                erros += 1
                print('\nPalavra não encontrada.')
                pontos_segundo_jogador -= 5

                if erros == 1:
                    print('\nO boneco possui cabeça e houve 1 tentativa.\n')
                    continue
                elif erros == 2:
                    print('\nO boneco possui cabeça e tronco e houve 2 tentativas.\n')
                    continue
                elif erros == 3:
                    print('\nO boneco possui cabeça, tronco e 1 braço e houve 3 tentativas.\n')
                    continue
                elif erros == 4:
                    print('\nO boneco possui cabeça, tronco e 2 braços e houve 4 tentativas.\n')
                    continue
                elif erros == 5:
                    print('\nO boneco possui cabeça, tronco, 2 braços e 1 perna e houve 5 tentativas.\n')
                    continue
                else:
                    print('\nO boneco possui cabeça, tronco, 2 braços e 2 pernas e houve 6 tentativas.\n')
                    print('\nSuas tentativas acabaram! Infelizmente, você não acertou a palavra.\n')
                    break

            tentativa_terceiro_jogador = input(f'\n{nome_terceiro_jogador}, digite uma letra: ').upper().split()[0] 

            if tentativa_terceiro_jogador in letras_digitadas:
                print('\nEssa letra já está na palavra! Tente outra...\n')
                pontos_terceiro_jogador -= 2
                continue

            letras_digitadas.append(tentativa_terceiro_jogador)

            if tentativa_terceiro_jogador in palavra_terceiro_jogador:
                for index, letra in enumerate(palavra_terceiro_jogador):
                    if letra == tentativa_terceiro_jogador:
                        estado_palavra[index] = tentativa_terceiro_jogador
                        pontos_terceiro_jogador += 10

                if '_' not in estado_palavra:
                    print('\nA palavra foi completada.')

                    if pontos_segundo_jogador > pontos_terceiro_jogador:
                        print(f'\nParabéns, {nome_segundo_jogador}! Você acertou a palavra.')
                        print(f'\nSegue o ranking:\n\n{nome_terceiro_jogador} - {pontos_terceiro_jogador} pontos\n{nome_segundo_jogador} - {pontos_segundo_jogador} pontos\n')

                    elif pontos_segundo_jogador < pontos_terceiro_jogador:
                        print(f'\nParabéns, {nome_terceiro_jogador}! Você acertou a palavra.')
                        print(f'\nSegue o ranking:\n\n{nome_segundo_jogador} - {pontos_segundo_jogador} pontos\n{nome_terceiro_jogador} - {pontos_terceiro_jogador} pontos\n')

                    else:
                        print('\nHouve um empate! Que curioso! Parabéns para ambos!\n')

                    break

            else:
                erros += 1
                print('\nPalavra não encontrada.')
                pontos_terceiro_jogador -= 5

                if erros == 1:
                    print('\nO boneco possui cabeça e houve 1 tentativa.\n')
                    continue
                elif erros == 2:
                    print('\nO boneco possui cabeça e tronco e houve 2 tentativas.\n')
                    continue
                elif erros == 3:
                    print('\nO boneco possui cabeça, tronco e 1 braço e houve 3 tentativas.\n')
                    continue
                elif erros == 4:
                    print('\nO boneco possui cabeça, tronco e 2 braços e houve 4 tentativas.\n')
                    continue
                elif erros == 5:
                    print('\nO boneco possui cabeça, tronco, 2 braços e 1 perna e houve 5 tentativas.\n')
                    continue
                else:
                    print('\nO boneco possui cabeça, tronco, 2 braços e 2 pernas e houve 6 tentativas.\n')
                    print('\nSuas tentativas acabaram! Infelizmente, você não acertou a palavra.\n')
                    break

    elif opcao_teceiro_jogador == 2:
        while erros < tentativas:
            print('Palavra:', ' '.join(estado_palavra))

            tentativa_segundo_jogador = input(f'\n{nome_segundo_jogador}, digite uma letra: ').upper().split()[0]

            if tentativa_segundo_jogador in letras_digitadas:
                print('\nEssa letra já está na palavra! Tente outra...\n')
                continue

            letras_digitadas.append(tentativa_segundo_jogador)

            if tentativa_segundo_jogador in palavra_terceiro_jogador:
                for index, letra in enumerate(palavra_terceiro_jogador):
                    if letra == tentativa_segundo_jogador:
                        estado_palavra[index] = tentativa_segundo_jogador
                        pontos_segundo_jogador += 10
                print('\n')

            else:
                erros += 1
                print('\nPalavra não encontrada.')

                if erros == 1:
                    print('\nO boneco possui cabeça e houve 1 tentativa.\n')
                    continue
                elif erros == 2:
                    print('\nO boneco possui cabeça e tronco e houve 2 tentativas.\n')
                    continue
                elif erros == 3:
                    print('\nO boneco possui cabeça, tronco e 1 braço e houve 3 tentativas.\n')
                    continue
                elif erros == 4:
                    print('\nO boneco possui cabeça, tronco e 2 braços e houve 4 tentativas.\n')
                    continue
                elif erros == 5:
                    print('\nO boneco possui cabeça, tronco, 2 braços e 1 perna e houve 5 tentativas.\n')
                    continue
                else:
                    print('\nO boneco possui cabeça, tronco, 2 braços e 2 pernas e houve 6 tentativas.\n')
                    print('\nSuas tentativas acabaram! Infelizmente, você não acertou a palavra.\n')
                    break

            if '_' not in estado_palavra:
                print('Palavra:', ' '.join(estado_palavra))
                print(f'\nParabéns, {nome_segundo_jogador}! Você acertou a palavra.')
                break

    else:
        print('\nOpção inválida!\n')

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

tema_terceiro_jogador = int(input('Diante às opções, escolha um tema: '))

while tema_terceiro_jogador != 0:

    if tema_terceiro_jogador == 1:
        print('')
        print(paises_forca.keys())
        
        palavra_terceiro_jogador = input('\nEscolha uma palavra: ').strip().upper() # '.strip()' remove espaços em branco e deixa em maiúsculo

        if palavra_terceiro_jogador in paises_forca:
            print('\nDica:', paises_forca[palavra_terceiro_jogador])

            estado_palavra = ['_' for _ in palavra_terceiro_jogador]

            print('\nO boneco se inicia vazio e com 0 tentativas.\n')    

            jogando_forca()

        else:
            print('\nPalavra não encontrada na lista.')
            continue

    elif tema_terceiro_jogador == 2:
        print('')
        print(frutas_forca.keys())
        
        palavra_terceiro_jogador = input('\nEscolha uma palavra: ').strip().upper()

        if palavra_terceiro_jogador in frutas_forca:
            print('\nDica:', frutas_forca[palavra_terceiro_jogador])

            estado_palavra = ['_' for _ in palavra_terceiro_jogador]

            print('\nO boneco se inicia vazio e com 0 tentativas.\n')    

            jogando_forca()

        else:
            print('\nPalavra não encontrada na lista.')
            continue

    elif tema_terceiro_jogador == 3:
        print('')
        print(objetos_forca.keys())
        
        palavra_terceiro_jogador = input('\nEscolha uma palavra: ').strip().upper()

        if palavra_terceiro_jogador in objetos_forca:
            print('\nDica:', objetos_forca[palavra_terceiro_jogador])

            estado_palavra = ['_' for _ in palavra_terceiro_jogador]

            print('\nO boneco se inicia vazio e com 0 tentativas.\n')    

            jogando_forca()

        else:
            print('\nPalavra não encontrada.')
            continue

    elif tema_terceiro_jogador == 4:
        print('')
        print(carros_forca.keys())
        
        palavra_terceiro_jogador = input('\nEscolha uma palavra: ').strip().upper()

        if palavra_terceiro_jogador in carros_forca:
            print('\nDica:', carros_forca[palavra_terceiro_jogador])

            estado_palavra = ['_' for _ in palavra_terceiro_jogador]

            print('\nO boneco se inicia vazio e com 0 tentativas.\n')    

            jogando_forca()

        else:
            print('\nPalavra não encontrada.')
            continue

    print('\n[1] PAÍSES\n[2] FRUTAS\n[3] OBJETOS\n[4] CARROS\n[0] SAIR\n')

    tema_terceiro_jogador = int(input('Diante às opções, escolha um tema: '))

if tema_terceiro_jogador == 0:
    print('\nObrigado por jogar! Até a próxima.\n')