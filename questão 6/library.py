import pandas as pd
from datetime import datetime, timedelta

locacao = datetime.today()
devolucao = locacao + timedelta(days=15)

ler_livros = pd.read_csv('questão 6/livros.csv')
ler_membros = pd.read_csv('questão 6/membros.csv')

pd.set_option('display.max_rows', None) # permite visualizar todas as linhas da tabela (o None não define limite nelas)
pd.set_option('display.max_columns', None) # permite visualizar todas as colunas da tabela (o None não define limite nelas)

coluna_autor = ler_livros['autores']
coluna_titulo = ler_livros['titulo']

quantidade_livro_emprestado = 0

coluna_matricula = ler_membros['matricula']
coluna_nome = ler_membros['nome']

membros_livros_locados = {}

while True:
    opcao = int(input("\nOlá! Seja bem-vindo ao acervo online da instituição!\n\n[1] - PEGAR LIVROS\n[2] - DEVOLVER LIVROS\n[3] - HISTÓRICO\n[4] - SAIR\n\nO que você gostaria de fazer? "))

    if opcao == 1:
        visualizar_livros = int(input("\n[1] - SIM\n[2] - NÃO\n\nDeseja visualizar os livros disponíveis para empréstimo? "))

        print()

        if visualizar_livros == 1:
            print(ler_livros)
            print("\n")

        livro_locacao = input("Digite o título ou autor do livro você deseja pegar emprestado: ")

        # verificação que não é sensível a maiúsculas ou minúsculas
        verificacao_autor = ler_livros['autores'].str.contains(livro_locacao, case=False)
        verificacao_livro = ler_livros['titulo'].str.contains(livro_locacao, case=False)

        if any(verificacao_livro):
            quantidade_livro_atual = ler_livros.loc[verificacao_livro, 'quantidade'].values[0] # verifica a quantidade de livros específicos

            if quantidade_livro_atual > 0:
                membro_locacao = int(input("\nDigite sua matrícula: "))

                if membro_locacao in membros_livros_locados and livro_locacao in membros_livros_locados[membro_locacao]:
                    print('\nO mesmo aluno não pode pegar o mesmo livro...\n')
                    print(membros_livros_locados)

                else:
                    if membro_locacao in coluna_matricula.values:
                        ler_livros.loc[verificacao_livro, 'quantidade'] -= 1
                        quantidade_livro_emprestado += 1

                        if membro_locacao in membros_livros_locados: # evita que seja criado outro array para o mesmo aluno
                            membros_livros_locados[membro_locacao].append((livro_locacao, locacao.strftime("%d/%m/%Y"), devolucao.strftime("%d/%m/%Y")))
                        else:
                            membros_livros_locados[membro_locacao] = [livro_locacao, locacao.strftime("%d/%m/%Y"), devolucao.strftime("%d/%m/%Y")]

                        print(f'\nLivro {livro_locacao} emprestado com sucesso!\n\nVocê o pegou emprestado dia {locacao.strftime("%d/%m/%Y")} e terá que devolvê-lo dia {devolucao.strftime("%d/%m/%Y")}!\n\nAproveite a leitura!\n')
                    else:
                        print('\nMembros não pertencentes à instituição não podem alocar livros...\n')
            else:
                print('\nTodos nossos livros desse título estão esgotados... Tente mais tarde!\n\n')

        elif any(verificacao_autor):
            livros_autor_especifico = ler_livros[verificacao_autor]
            print()
            print(livros_autor_especifico[['titulo', 'quantidade']])

            livro_locacao_autor = input('\nEscolha 1 livro que pertencem a esse autor para fazer a locação: ')

            if livro_locacao_autor.lower() in livros_autor_especifico['titulo'].str.lower().values:
                quantidade_livro_atual = livros_autor_especifico.loc[livros_autor_especifico['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'].values[0] 

                if quantidade_livro_atual > 0:
                    membro_locacao = int(input("\nDigite sua matrícula: "))

                    if coluna_matricula.isin([membro_locacao]).any(): # verifica se a matrícula digitada está na lista de membros e retona True ou False
                        if membro_locacao in membros_livros_locados and livro_locacao_autor in [livro[0] for livro in membros_livros_locados[membro_locacao]]:
                            print('\nO mesmo aluno não pode pegar o mesmo livro...')
                        else:
                            if membro_locacao in coluna_matricula.values:
                                ler_livros.loc[ler_livros['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'] -= 1
                                membros_livros_locados.setdefault(membro_locacao, []).append((livro_locacao_autor, locacao.strftime("%d/%m/%Y"), devolucao.strftime("%d/%m/%Y"))) # adiciona um registro de empréstimo para o membro, com informações sobre o livro, data de locação e data de devolução
                                print(f'\nLivro {livro_locacao_autor} emprestado com sucesso!\n\nVocê o pegou emprestado dia {locacao.strftime("%d/%m/%Y")} e terá que devolvê-lo dia {devolucao.strftime("%d/%m/%Y")}!\n\nAproveite a leitura!')           
                    else:
                        print('\nMembros não pertencentes à instituição não podem alocar livros...')
                else:
                    print('\nTodos nossos livros desse título foram esgotados...')
            else:
                print('\nLivro não encontrado...')
        else:
            print("\nAutor ou livro não encontrado...")

    elif opcao == 2:
        livro_locacao = input("\nDigite o título ou autor do livro você está devolvendo: ")

        # verificação que não é sensível a maiúsculas ou minúsculas
        verificacao_autor = ler_livros['autores'].str.contains(livro_locacao, case=False)
        verificacao_livro = ler_livros['titulo'].str.contains(livro_locacao, case=False)

        if any(verificacao_livro):
            quantidade_livro_atual = ler_livros.loc[verificacao_livro, 'quantidade'].values[0] # verifica a quantidade de livros específicos

            if quantidade_livro_atual > 0:
                membro_locacao = int(input("\nDigite sua matrícula: "))
                
                if membro_locacao in membros_livros_locados and any(livro[0].lower() == livro_locacao.lower() for livro in membros_livros_locados[membro_locacao]):
                    if devolucao.strftime("%d/%m/%Y") <= datetime.today().strftime("%d/%m/%Y"):
                        ler_livros.loc[verificacao_livro, 'quantidade'] += 1
                        quantidade_livro_emprestado -= 1

                        membros_livros_locados[membro_locacao] = [livro for livro in membros_livros_locados[membro_locacao] if livro[0].lower() != livro_locacao.lower()] # remove o livro da lista de locação
                        
                        print(f'\nLivro {livro_locacao} devolvido com sucesso!\n\nObrigado por devolvê-lo!')
                        
                    else:
                        print(f'\nLivro {livro_locacao} devolvido com atraso!\n\nVocê terá que pagar uma multa de R$ {10 * int(datetime.today().strftime("%d")) - (int(devolucao.strftime("%d")))} reais.\n\nObrigado por devolvê-lo!')
                else:
                    print('\nLivro não foi locado por você...')
            else:
                    print('\nLivro não encontrado...')

        elif any(verificacao_autor):
            livros_autor_especifico = ler_livros[verificacao_autor]
            livro_locacao_autor = input('\nDiga o nome livro que pertencem a esse autor para fazer a devolução: ')

            if livro_locacao_autor in livros_autor_especifico['titulo'].str.lower().values:
                quantidade_livro_atual = livros_autor_especifico.loc[livros_autor_especifico['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'].values[0] 

                if quantidade_livro_atual > 0:
                    membro_locacao = int(input("\nDigite sua matrícula: "))
                
                    if membro_locacao in membros_livros_locados and any(livro[0].lower() == livro_locacao_autor.lower() for livro in membros_livros_locados[membro_locacao]):
                        if devolucao.strftime("%d/%m/%Y") <= datetime.today().strftime("%d/%m/%Y"):
                            ler_livros.loc[ler_livros['titulo'].str.lower() == livro_locacao_autor, 'quantidade'] += 1
                            quantidade_livro_emprestado -= 1

                            membros_livros_locados[membro_locacao] = [livro for livro in membros_livros_locados[membro_locacao] if livro[0].lower() != livro_locacao_autor]

                            print(f'\nLivro {livro_locacao} devolvido com sucesso!\n\nObrigado por devolvê-lo!')
                        else:
                            print(f'\nLivro {livro_locacao} devolvido com atraso!\n\nVocê terá que pagar uma multa de R$ {10 * int(datetime.today().strftime("%d")) - (int(devolucao.strftime("%d")))} reais.\n\nObrigado por devolvê-lo!')
                    else:
                        print('\nLivro não foi locado por você...')
                else:
                    print('\nLivro não encontrado...')
            else:
                print("\nAutor ou livro não encontrado...\n")

    elif opcao == 3:
        if not membros_livros_locados:
            print("\nNenhum histórico de empréstimos encontrado.\n")
        else:
            membro_locacao = int(input("\nDigite sua matrícula para visualizar seu histórico: "))

            if membro_locacao in membros_livros_locados:
                print(f"\nHistórico de Empréstimos para a matrícula {membro_locacao}:\n")
                for livro, data_locacao, data_devolucao in membros_livros_locados[membro_locacao]:
                    data_devolucao_dt = datetime.strptime(data_devolucao, "%d/%m/%Y")
                    dias_atraso = (datetime.today() - data_devolucao_dt).days
                    
                    multa = 10 * dias_atraso if dias_atraso > 0 else 0
                    
                    print(f"Livro: {livro}")
                    print(f"Data de Locação: {data_locacao}")
                    print(f"Data de Devolução Prevista: {data_devolucao}")
                    print(f"Dias de Atraso: {dias_atraso if dias_atraso > 0 else 0}")
                    print(f"Total a Pagar: R$ {multa:.2f}\n")
            else:
                print("\nMatrícula não encontrada no histórico de empréstimos.\n")
                
    elif opcao == 4:
        print('\nAté mais!\n\nSaindo...\n')
        break

    else:
        print('\nOpção inválida!\n')
        continue