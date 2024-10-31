def decimal_para_romano(numero_decimal):
    dicionario_romano = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    
    resultado = ''
    
    for valor in sorted(dicionario_romano.keys(), reverse=True):
        while numero_decimal >= valor:
            resultado += dicionario_romano[valor]
            numero_decimal -= valor
    return resultado

def romano_para_decimal(numero_romano):
    dicionario_decimal = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
        'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    
    resultado = 0
    i = 0
    
    while i < len(numero_romano):
        if i + 1 < len(numero_romano) and numero_romano[i:i + 2] in dicionario_decimal:
            resultado += dicionario_decimal[numero_romano[i:i + 2]]
            i += 2
        elif numero_romano[i] in dicionario_decimal:
            resultado += dicionario_decimal[numero_romano[i]]
            i += 1
        else:
            print("\nNúmero romano inválido.")
            return None
    return resultado

while True:
    try:
        opcao = int(input('\nDeseja converter [1] DECIMAL PARA ROMANO ou [2] ROMANO PARA DECIMAL?\n\n[0] SAIR\n\nResposta: '))
    except ValueError:
        print("\nOpção inválida! Por favor, insira um número entre 0 e 2.")
        continue

    if opcao == 1:
        try:
            numero_decimal = int(input('\nDigite um número decimal para ser convertido em romano: '))
            if numero_decimal <= 0 or numero_decimal > 3999:
                print("\nNúmero fora do intervalo (1-3999).")
                continue
            print('\nO número em romano é:', decimal_para_romano(numero_decimal))
        except ValueError:
            print("\nEntrada inválida! Digite um número decimal válido.")
            
    elif opcao == 2:
        numero_romano = input('\nDigite um número romano para ser convertido em decimal: ').upper()
        if all(c in 'IVXLCDM' for c in numero_romano):  # Verifica caracteres válidos
            resultado = romano_para_decimal(numero_romano)
            if resultado and 1 <= resultado <= 3999:
                print('\nO número em decimal é:', resultado)
            else:
                print("\nNúmero fora do intervalo (1-3999) ou inválido.")
        else:
            print("\nEntrada inválida! Use apenas caracteres romanos válidos (I, V, X, L, C, D, M).")
            
    elif opcao == 0:
        print('\nPrograma encerrado!\n')
        break
    else:
        print("\nOpção inválida! Por favor, selecione 0, 1 ou 2.")
