def exibir_forca(erros):
    if erros == 1:
        print('\nO boneco possui cabeça e houve 1 tentativa.\n')
    elif erros == 2:
        print('\nO boneco possui cabeça e tronco e houve 2 tentativas.\n')
    elif erros == 3:
        print('\nO boneco possui cabeça, tronco e 1 braço e houve 3 tentativas.\n')
    elif erros == 4:
        print('\nO boneco possui cabeça, tronco e 2 braços e houve 4 tentativas.\n')
    elif erros == 5:
        print('\nO boneco possui cabeça, tronco, 2 braços e 1 perna e houve 5 tentativas.\n')
    elif erros == 6:
        print('\nO boneco possui cabeça, tronco, 2 braços e 2 pernas e houve 6 tentativas.\n')

def processar_palavra_jogador(letra, palavra, estado_palavra, pontos):
    if letra in palavra:
        for index, char in enumerate(palavra):
            if char == letra:
                estado_palavra[index] = letra
        pontos += 10
    else:
        pontos -= 5
    return pontos

def verificar_vencedor(pontos_segundo_jogador, pontos_terceiro_jogador, nome_segundo_jogador, nome_terceiro_jogador):
    if pontos_segundo_jogador > pontos_terceiro_jogador:
        print(f'\nParabéns, {nome_segundo_jogador}! Você venceu.')
        print(f'\nSegue o ranking:\n\n{nome_segundo_jogador} - {pontos_segundo_jogador} pontos\n{nome_terceiro_jogador} - {pontos_terceiro_jogador} pontos\n')
    elif pontos_terceiro_jogador > pontos_segundo_jogador:
        print(f'\nParabéns, {nome_terceiro_jogador}! Você venceu.')
        print(f'\nSegue o ranking:\n\n{nome_terceiro_jogador} - {pontos_terceiro_jogador} pontos\n{nome_segundo_jogador} - {pontos_segundo_jogador} pontos\n')
    else:
        print('\nHouve um empate! Parabéns a ambos!\n')

def jogar_forca_com_um_jogador(nome_segundo_jogador, palavra_terceiro_jogador, estado_palavra, letras_digitadas):
    erros = 0
    tentativas = 6
    pontos_segundo_jogador = 0

    while erros < tentativas:
        print('\nPalavra:', ' '.join(estado_palavra))

        tentativa = input(f'\n{nome_segundo_jogador}, digite uma letra: ').upper().strip()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("\nDigite apenas uma letra válida.\n")
            continue

        if tentativa in letras_digitadas:
            print('\nEssa letra já foi digitada! Tente outra...\n')
            continue

        letras_digitadas.append(tentativa)

        pontos_segundo_jogador = processar_palavra_jogador(tentativa, palavra_terceiro_jogador, estado_palavra, pontos_segundo_jogador)

        if tentativa not in palavra_terceiro_jogador:
            erros += 1
            exibir_forca(erros)

        if '_' not in estado_palavra:
            print('\nPalavra:', ' '.join(estado_palavra))
            print(f'\nParabéns, {nome_segundo_jogador}! Você acertou a palavra.')
            break

def jogar_forca_com_dois_jogadores(nome_segundo_jogador, nome_terceiro_jogador, palavra_terceiro_jogador, estado_palavra, letras_digitadas):
    erros = 0
    tentativas = 6
    pontos_segundo_jogador = 0
    pontos_terceiro_jogador = 0

    while erros < tentativas:
        print('\nPalavra:', ' '.join(estado_palavra))

        # Jogador 1
        tentativa_segundo_jogador = input(f'\n{nome_segundo_jogador}, digite uma letra: ').upper().split()[0]

        if tentativa_segundo_jogador in letras_digitadas:
            print('\nEssa letra já foi digitada! Tente outra...\n')
            pontos_segundo_jogador -= 2
            continue

        letras_digitadas.append(tentativa_segundo_jogador)
        pontos_segundo_jogador = processar_palavra_jogador(tentativa_segundo_jogador, palavra_terceiro_jogador, estado_palavra, pontos_segundo_jogador)

        if tentativa_segundo_jogador not in palavra_terceiro_jogador:
            erros += 1
            exibir_forca(erros)

        if '_' not in estado_palavra:
            print('\nPalavra:', ' '.join(estado_palavra))
            verificar_vencedor(pontos_segundo_jogador, pontos_terceiro_jogador, nome_segundo_jogador, nome_terceiro_jogador)
            break

        # Jogador 2
        tentativa_terceiro_jogador = input(f'\n{nome_terceiro_jogador}, digite uma letra: ').upper().split()[0]

        if tentativa_terceiro_jogador in letras_digitadas:
            print('\nEssa letra já foi digitada! Tente outra...\n')
            pontos_terceiro_jogador -= 2
            continue

        letras_digitadas.append(tentativa_terceiro_jogador)
        pontos_terceiro_jogador = processar_palavra_jogador(tentativa_terceiro_jogador, palavra_terceiro_jogador, estado_palavra, pontos_terceiro_jogador)

        if tentativa_terceiro_jogador not in palavra_terceiro_jogador:
            erros += 1
            exibir_forca(erros)

        if '_' not in estado_palavra:
            print('\nPalavra:', ' '.join(estado_palavra))
            verificar_vencedor(pontos_segundo_jogador, pontos_terceiro_jogador, nome_segundo_jogador, nome_terceiro_jogador)
            break

def iniciar_jogo():
    while True:
        try:
            print('\n[1] PAÍSES\n[2] FRUTAS\n[3] OBJETOS\n[4] CARROS\n[0] SAIR\n')
            tema_terceiro_jogador = int(input('Escolha um tema: '))
        except ValueError:
            print("\nOpção inválida! Digite um número de 0 a 4.")
            continue

        if tema_terceiro_jogador == 0:
            print('\nObrigado por jogar! Até a próxima.')
            break

        tema = {
            1: ('PAÍSES', paises_forca),
            2: ('FRUTAS', frutas_forca),
            3: ('OBJETOS', objetos_forca),
            4: ('CARROS', carros_forca)
        }

        if tema_terceiro_jogador in tema:
            _, categoria = tema[tema_terceiro_jogador]
            print(list(categoria.keys()))

            palavra_terceiro_jogador = input('\nEscolha uma palavra: ').strip().upper()
            if palavra_terceiro_jogador in categoria:
                print('\nDica:', categoria[palavra_terceiro_jogador])
                estado_palavra = ['_' for _ in palavra_terceiro_jogador]
                print('\nO boneco se inicia vazio e com 0 tentativas.\n')

                nome_segundo_jogador = input('Digite o nome do 1º jogador: ').split()[0]
                
                while True:
                    try:
                        opcao_teceiro_jogador = int(input('\n[1] SIM\n[2] NÃO\n\nDeseja adicionar mais de 1 jogador? '))
                        if opcao_teceiro_jogador not in [1, 2]:
                            raise ValueError
                        break
                    except ValueError:
                        print("\nDigite apenas 1 para SIM ou 2 para NÃO.")

                if opcao_teceiro_jogador == 1:
                    nome_terceiro_jogador = input('\nDigite o nome do 2º jogador: ').split()[0]
                    jogar_forca_com_dois_jogadores(nome_segundo_jogador, nome_terceiro_jogador, palavra_terceiro_jogador, estado_palavra, [])
                else:
                    jogar_forca_com_um_jogador(nome_segundo_jogador, palavra_terceiro_jogador, estado_palavra, [])
            else:
                print('\nPalavra não encontrada.')
        else:
            print("\nOpção de tema inválida. Tente novamente.")

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

iniciar_jogo()