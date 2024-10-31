import random
import pygame

pygame.mixer.init()
som_urna = pygame.mixer.Sound('C:/Users/06006399/Desktop/necessary-algorithms/questão 5/som_urna_eletronica.mp3')

def som_urna_eletronica():
    som_urna.play()

def cadastro_candidatos():
    nome_candidato = input('\nDigite seu nome de candidato: ')
    
    identificacoes_possiveis = random.sample(range(100, 1000), 90)  # Gera uma lista de números aleatórios únicos
    identificacao_sorteada = identificacoes_possiveis.pop()

    candidatos[nome_candidato] = {
        'identificacao_sorteada': identificacao_sorteada,
        'quantidade_votos': 0
    }
    
    print(f'\nCandidato cadastrado! Seu número de identificação é: {identificacao_sorteada}\n')

def cadastro_eleitores():
    identificacao_eleitor = input('\nDigite seu CPF (apenas números): ')
    
    if len(identificacao_eleitor) == 11 and identificacao_eleitor.isdigit():
        senha_eleitor = input('\nCrie uma senha: ')
        
        eleitores[identificacao_eleitor] = {
            'senha_eleitor': senha_eleitor,
            'voto_repetido': False
        }
        
        print('\nCadastro de eleitor realizado!\n')
    else:
        print('\nNúmero inválido para CPF!\n')

def registro_votos():
    global votos_validos, votos_brancos, votos_nulos

    acesso_eleitor_identificacao = input('\nDigite seu CPF para acessar a urna: ')
    acesso_eleitor_senha = input('\nDigite sua senha para acessar a urna: ')
    
    if acesso_eleitor_identificacao in eleitores.keys() and eleitores[acesso_eleitor_identificacao]['senha_eleitor'] == acesso_eleitor_senha:
        if eleitores[acesso_eleitor_identificacao]['voto_repetido']:
            print('\nVocê já votou!\n')
        else:
            voto = input('\nRegistre o número de identificação do candidato ou "BRANCO" para voto branco: ').upper()

            if voto in [str(candidato['identificacao_sorteada']) for candidato in candidatos.values()]:
                for nome, dados in candidatos.items():
                    if dados['identificacao_sorteada'] == int(voto):
                        nome_candidato = nome
                        break

                som_urna_eletronica()
                votos_validos += 1 
                candidatos[nome_candidato]['quantidade_votos'] += 1
                eleitores[acesso_eleitor_identificacao]['voto_repetido'] = True
            elif voto == 'BRANCO': # voto branco
                som_urna_eletronica()
                votos_brancos += 1
            else: # voto nulo
                som_urna_eletronica()
                votos_nulos += 1
    else:
        print('\nEleitor não encontrado! Tente se cadastrar antes...\n')

def relatorio_final():
    print(f'\nVOTOS VÁLIDOS: {votos_validos}\nVOTOS BRANCOS: {votos_brancos}\nVOTOS NULOS: {votos_nulos}')

    resultado_candidato = dict(sorted(candidatos.items(), key=lambda item: item[1]['quantidade_votos'], reverse=True))
    print(f'\nResultado final:\n')
    for nome, dados in resultado_candidato.items():
        print(f'{nome}: {dados}')
        print()

    candidato_elegido = list(resultado_candidato.keys())[0] if resultado_candidato else "nenhum"

    max_votos = None
    empatados = []

    for nome, dados in resultado_candidato.items():
        if max_votos is None or dados['quantidade_votos'] == max_votos:
            max_votos = dados['quantidade_votos']
            empatados.append(nome)
        elif dados['quantidade_votos'] < max_votos:
            break 

    if len(empatados) > 1:
        print(f'\nHouve um empate entre os candidatos: {", ".join(empatados)} com {max_votos} votos! Teremos 2º turno...')
    elif empatados:
        candidato_elegido = empatados[0]
        print(f'\nO candidato eleito foi {candidato_elegido} com {max_votos} votos!')
    else:
        print('\nNenhum candidato foi eleito.')

candidatos = {}
eleitores = {}

votos_validos = 0
votos_brancos = 0
votos_nulos = 0

while True:
    try:
        opcao = int(input('\n[1] CADASTRO DE CANDIDATOS\n[2] CADASTRO DE ELEITORES\n[3] REGISTRAR VOTOS\n[4] RELATÓRIO FINAL\n[0] SAIR\n\nEscolha uma opção: '))
    except ValueError:
        print('\nOpção inválida! Por favor, insira um número.')
        continue

    if opcao == 1:
        cadastro_candidatos()
    elif opcao == 2:
        cadastro_eleitores()
    elif opcao == 3:
        registro_votos()
    elif opcao == 4:
        relatorio_final()
    elif opcao == 0:
        som_urna_eletronica()
        print('\nSaindo...\n')
        break
    else:
        print('\nOpção inválida! Por favor, escolha uma opção válida.\n')
