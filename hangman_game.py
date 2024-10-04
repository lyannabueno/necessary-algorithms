paises_forca = {
    'Brasil': 'Copa do Mundo de 2002',
    'França': 'Copa do Mundo de 1998',
    'Espanha': 'Copa do Mundo de 2010'
}

frutas_forca = {
    'Banana': 'Fruta amarela',
    'Maçã': 'Fruta vermelha',
    'Uva': 'Fruta roxa'
}

objetos_forca = {
    'Cadeira': 'Objeto para sentar',
    'Cama': 'Objeto para dormir',
    'Geladeira': 'Objeto para armazenar alimentos'
}

carros_forca = {
    'Fusca': 'Carro popular',
    'Ferrari': 'Carro esportivo',
    'Camaro': 'Carro americano'
}

print('[1] PAÍSES\n[2] FRUTAS\n[3] OBJETOS\n[4] CARROS\n[0] SAIR\n')

escolha_tema = str(input('Diante às opções, escolha um tema: '))

if escolha_tema == 1:
    print(paises_forca.keys())
    
    escolha_palavra = str(input('Escolha uma palavra: '))
    
    if escolha_palavra == paises_forca[0]:
        print('Dica:', paises_forca.values())
    else:
        print('Palavra não encontrada.')
        
    for i in range(6): # braços, pernas, cabeça, tronco
        print('O boneco tem inicia vazio e com', i, 'tentativas.\n\n')
        
        estado_palavra = ['_' for i in escolha_palavra]
        
        palavra_usuario = str(input('Digite uma letra: '))
        
        if palavra_usuario[i] in escolha_palavra:
            for index, letra in enumerate(escolha_palavra):
                if letra == palavra_usuario:
                    escolha_palavra[index] = palavra_usuario
        else:
            print('Palavra não encontrada.')
            
        print('Palavra:', ' '.join(estado_palavra))
        
        if '_' not in estado_palavra:
            print('Parabéns! Você acertou a palavra.')
            break
    else:
        print('Infelizmente, você não acertou a palavra.')