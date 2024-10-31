import pandas as pd
from datetime import datetime, timedelta

locacao = datetime.today()
devolucao = locacao + timedelta(days=15)

ler_livros = pd.read_csv('questão 6/livros.csv')
ler_membros = pd.read_csv('questão 6/membros.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

coluna_autor = ler_livros['autores']
coluna_titulo = ler_livros['titulo']
coluna_matricula = ler_membros['matricula']
coluna_nome = ler_membros['nome']

membros_livros_locados = {}

while True:
    try:
        opcao = int(input("\nOlá! Seja bem-vindo ao acervo online da instituição!\n\n[1] - PEGAR LIVROS\n[2] - DEVOLVER LIVROS\n[3] - HISTÓRICO\n[4] - SAIR\n\nO que você gostaria de fazer? "))
    except ValueError:
        print("\nEntrada inválida! Por favor, escolha uma opção numérica.")
        continue

    if opcao == 1:
        try:
            visualizar_livros = int(input("\n[1] - SIM\n[2] - NÃO\n\nDeseja visualizar os livros disponíveis para empréstimo? "))
        except ValueError:
            print("\nEntrada inválida! Por favor, escolha uma opção numérica.")
            continue

        if visualizar_livros == 1:
            print(ler_livros)

        livro_locacao = input("Digite o título ou autor do livro que deseja pegar emprestado: ")

        verificacao_autor = ler_livros['autores'].str.contains(livro_locacao, case=False)
        verificacao_livro = ler_livros['titulo'].str.contains(livro_locacao, case=False)

        if any(verificacao_livro):
            quantidade_livro_atual = ler_livros.loc[verificacao_livro, 'quantidade'].values[0]

            if quantidade_livro_atual > 0:
                try:
                    membro_locacao = int(input("\nDigite sua matrícula: "))
                except ValueError:
                    print("\nEntrada inválida! A matrícula deve ser um número.")
                    continue

                if membro_locacao in coluna_matricula.values:
                    if membro_locacao in membros_livros_locados and livro_locacao in [livro[0] for livro in membros_livros_locados[membro_locacao]]:
                        print('\nO mesmo aluno não pode pegar o mesmo livro novamente.\n')
                    else:
                        ler_livros.loc[verificacao_livro, 'quantidade'] -= 1
                        membros_livros_locados.setdefault(membro_locacao, []).append((livro_locacao, locacao.strftime("%d/%m/%Y"), devolucao.strftime("%d/%m/%Y")))
                        print(f'\nLivro {livro_locacao} emprestado com sucesso!\nPegue-o no dia {locacao.strftime("%d/%m/%Y")} e devolva-o até {devolucao.strftime("%d/%m/%Y")}!\nAproveite a leitura!\n')
                else:
                    print('\nA matrícula informada não pertence a nenhum membro da instituição.\n')
            else:
                print('\nTodos os exemplares deste livro estão esgotados. Tente novamente mais tarde.\n')
                
        elif any(verificacao_autor):
            livros_autor_especifico = ler_livros[verificacao_autor]
            print(livros_autor_especifico[['titulo', 'quantidade']])

            livro_locacao_autor = input('\nEscolha um dos livros deste autor para locação: ')

            if livro_locacao_autor.lower() in livros_autor_especifico['titulo'].str.lower().values:
                quantidade_livro_atual = livros_autor_especifico.loc[livros_autor_especifico['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'].values[0]

                if quantidade_livro_atual > 0:
                    try:
                        membro_locacao = int(input("\nDigite sua matrícula: "))
                    except ValueError:
                        print("\nEntrada inválida! A matrícula deve ser um número.")
                        continue

                    if membro_locacao in coluna_matricula.values:
                        if membro_locacao in membros_livros_locados and livro_locacao_autor in [livro[0] for livro in membros_livros_locados[membro_locacao]]:
                            print('\nO mesmo aluno não pode pegar o mesmo livro novamente.\n')
                        else:
                            ler_livros.loc[ler_livros['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'] -= 1
                            membros_livros_locados.setdefault(membro_locacao, []).append((livro_locacao_autor, locacao.strftime("%d/%m/%Y"), devolucao.strftime("%d/%m/%Y")))
                            print(f'\nLivro {livro_locacao_autor} emprestado com sucesso!\nPegue-o no dia {locacao.strftime("%d/%m/%Y")} e devolva-o até {devolucao.strftime("%d/%m/%Y")}!\nAproveite a leitura!\n')
                    else:
                        print('\nA matrícula informada não pertence a nenhum membro da instituição.\n')
                else:
                    print('\nTodos os exemplares deste título estão esgotados.\n')
            else:
                print('\nLivro não encontrado.\n')
        else:
            print("\nLivro ou autor não encontrado.\n")

    elif opcao == 2:
        livro_locacao = input("\nDigite o título ou autor do livro que deseja devolver: ")

        verificacao_autor = ler_livros['autores'].str.contains(livro_locacao, case=False)
        verificacao_livro = ler_livros['titulo'].str.contains(livro_locacao, case=False)

        if any(verificacao_livro) or any(verificacao_autor):
            try:
                membro_locacao = int(input("\nDigite sua matrícula: "))
            except ValueError:
                print("\nEntrada inválida! A matrícula deve ser um número.")
                continue

            if membro_locacao in membros_livros_locados and any(livro[0].lower() == livro_locacao.lower() for livro in membros_livros_locados[membro_locacao]):
                data_devolucao = datetime.strptime(membros_livros_locados[membro_locacao][0][2], "%d/%m/%Y")
                dias_atraso = (datetime.today() - data_devolucao).days
                multa = max(0, dias_atraso) * 10

                ler_livros.loc[verificacao_livro | verificacao_autor, 'quantidade'] += 1
                membros_livros_locados[membro_locacao] = [livro for livro in membros_livros_locados[membro_locacao] if livro[0].lower() != livro_locacao.lower()]
                print(f'\nLivro {livro_locacao} devolvido com sucesso!\nMulta a pagar: R$ {multa:.2f}.\nObrigado por devolvê-lo!')
            else:
                print('\nVocê não locou este livro.\n')

        else:
            print("\nLivro ou autor não encontrado.\n")

    elif opcao == 3:
        try:
            membro_locacao = int(input("\nDigite sua matrícula para visualizar o histórico: "))
        except ValueError:
            print("\nEntrada inválida! A matrícula deve ser um número.")
            continue

        if membro_locacao in membros_livros_locados:
            print(f"\nHistórico de Empréstimos para a matrícula {membro_locacao}:\n")
            for livro, data_locacao, data_devolucao in membros_livros_locados[membro_locacao]:
                data_devolucao_dt = datetime.strptime(data_devolucao, "%d/%m/%Y")
                dias_atraso = (datetime.today() - data_devolucao_dt).days
                multa = max(0, dias_atraso) * 10

                print(f"Livro: {livro}")
                print(f"Data de Locação: {data_locacao}")
                print(f"Data de Devolução Prevista: {data_devolucao}")
                print(f"Dias de Atraso: {max(0, dias_atraso)}")
                print(f"Multa Total: R$ {multa:.2f}\n")
        else:
            print("\nNenhum histórico de empréstimos encontrado para esta matrícula.\n")

    elif opcao == 4:
        print('\nAté mais! Saindo...\n')
        break

    else:
        print('\nOpção inválida! Tente novamente.\n')
