opcao = int(input('\nDeseja converter [1] DECIMAL PARA ROMANO ou [2] ROMANO PARA DECIMAL?\n\n[0] SAIR\n\nReposta: '))

while opcao == 1 or opcao == 2 or opcao == 0:
    if opcao == 1:
        numero_decimal = int(input('\nDigite um número decimal para ser convertido em romano: '))

        dicionario_romano = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }

        if numero_decimal <= 0 or numero_decimal > 3999:
            print("\nNúmero fora do intervalo (1-3999).")

        else:
            resultado = ''

            for listagem_dicionario in sorted(dicionario_romano.keys(), reverse=True): # ordem descrescente para pegar o maior valor
                while numero_decimal >= listagem_dicionario:
                    resultado += dicionario_romano[listagem_dicionario] # converte o valor decimal em romano e adiciona à variável
                    numero_decimal -= listagem_dicionario # reduz do número decimal o valor convertido
            
            print('\nO número em romano é:', resultado)

    elif opcao == 2:
        numero_romano = input('\nDigite um número romano para ser convertido em decimal: ')

        dicionario_decimal = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }

        if not char in numero_romano:
            print("\nNúmero inválido.")

        else:
            for chave in dicionario_decimal.keys():
                if numero_romano == chave:
                    print(f'\nO valor de {numero_romano} convertido em decimal fica: {dicionario_decimal[chave]}')
                    continue

    elif opcao == 0:
        print('\nPrograma encerrado!\n')
        break

    else:
        print('\nOpção inválida.\n')

    opcao = int(input('\nDeseja converter [1] DECIMAL PARA ROMANO ou [2] ROMANO PARA DECIMAL?\n\nReposta: '))