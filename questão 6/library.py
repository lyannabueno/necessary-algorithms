import csv

acesso_livros = open('questão 6/livros.csv', 'r')
acesso_membros = open('questão 6/membros.csv', 'r')

ler_livros = csv.reader(acesso_livros)
ler_membros = csv.reader(acesso_membros)

opcao = int(input("\nOlá! Seja bem-vindo ao acervo online da instituição!\n\n[1] - PEGAR LIVROS\n[2] - DEVOLVER LIVROS\n[3] - SAIR\n\nO que você gostaria de fazer? "))

if opcao == 1:
    visualizar_livros = int(input("\n[1] - SIM\n[2] - NÃO\n\nDeseja visualizar os livros disponíveis para empréstimo? "))
    
    if visualizar_livros == 1:
        for linha in ler_livros:
            print(linha)
        print("\n")
    livro = input("Qual livro você deseja pegar emprestado? ")
    for linha in ler_membros:
        print(linha)
    print("\n")
    membro = input("Qual é o seu nome? ")
    print("\nLivro emprestado com sucesso! Aproveite a leitura!\n")