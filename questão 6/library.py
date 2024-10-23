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

while True:
    opcao = int(input("\nOlá! Seja bem-vindo ao acervo online da instituição!\n\n[1] - PEGAR LIVROS\n[2] - DEVOLVER LIVROS\n[3] - SAIR\n\nO que você gostaria de fazer? "))

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
                membro_locacao = int(input("\nDigite sua matrícula: ")) # impedir que o mesmo aluno pegue o mesmo livro 2x

                if membro_locacao in coluna_matricula.values:
                    ler_livros.loc[verificacao_livro, 'quantidade'] -= 1
                    quantidade_livro_emprestado += 1
                    print(f'\nLivro {livro_locacao} emprestado com sucesso!\n\nVocê o pegou emprestado dia {locacao.strftime("%d/%m/%Y")} e terá que devolvê-lo dia {devolucao.strftime("%d/%m/%Y")}!\n\nAproveite a leitura!\n')
                else:
                    print('\nMembros não pertencentes à instituição não podem alocar livros...\n')
            else:
                print('\nTodos nossos livros desse título estão esgotados... Tente mais tarde!\n\n')

        elif any(verificacao_autor):
            livros_autor_especifico = ler_livros[verificacao_autor]
            print()
            print(livros_autor_especifico)

            livro_locacao_autor = input('\nEscolha 1 livro que pertencem a esse autor para fazer a locação: ')

            if livro_locacao_autor.lower() in livros_autor_especifico['titulo'].str.lower().values:
                quantidade_livro_atual = livros_autor_especifico.loc[livros_autor_especifico['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'] 

                if not quantidade_livro_atual.empty:
                    quantidade_livro_atual = quantidade_livro_atual.values[0]  # acessa o primeiro valor da série

                    if quantidade_livro_atual > 0:
                        membro_locacao = int(input("\nDigite sua matrícula: "))

                        if membro_locacao in coluna_matricula.values:
                            livros_autor_especifico.loc[livros_autor_especifico['titulo'].str.lower() == livro_locacao_autor.lower(), 'quantidade'] -= 1
                            print(f'\nLivro {livro_locacao_autor} emprestado com sucesso!\n\nVocê o pegou emprestado dia {locacao.strftime("%d/%m/%Y")} e terá que devolvê-lo dia {devolucao.strftime("%d/%m/%Y")}!\n\nAproveite a leitura!\n')
                        else:
                            print('\nMembros não pertencentes à instituição não podem alocar livros...\n')
                    else:
                        print('Todos nossos livros desse título foram esgotados...')
                else:
                    print('\nLivro não encontrado...\n')
        else:
            print("\nAutor ou livro não encontrado...\n")

    elif opcao == 2: # escrever o código da devolução
        pass

    elif opcao == 3:
        print('\nAté mais!\n\nSaindo...\n')
        break

    else:
        print('\nOpção inválida!\n')
        continue