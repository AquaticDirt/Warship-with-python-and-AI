def printMapa(letrasLinhas, mapaJ):
    print('  |', end= ' ')
    for num in range(1, len(letrasLinhas) + 1):
        print(num, end= ' ')
    print('|')
    print('--+-----------------+')
    for i in range(len(mapaJ)):
        print(*letrasLinhas[i],'|',*mapaJ[i],'|')
    print('--+-----------------+')

def escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ):
    barcoEscolha = int(input('Sua escolha (1 a 5): '))
    if 1 <= barcoEscolha <= 5 and barcoEscolha not in barcosUsadosJ:
        while True:
            barcoPosicao = (input(f'Escolha uma posição inicial para o seu barco: {barcoEscolha}. {listaNomes[barcoEscolha-1]} (Ex.: D4): ')).upper()
            idx = 0
            if barcoPosicao[0] in letrasLinhas:
                while barcoPosicao[0] != letrasLinhas[idx]:
                    idx+=1
            barcoDir = input('Escolha a direção do barco (V para vertical, H para horizontal): ').upper()
            if barcoDir=='V' or barcoDir=='H':
                if barcoDir=='H':
                    if int(barcoPosicao[1]) + int(dictValores[f'b{barcoEscolha}'][0]) < 8:
                        for t in range(int(dictValores[f'b{barcoEscolha}'][0])):
                            if t == 0:
                                mapaJ[idx][int(barcoPosicao[1])-1] = '<'
                            elif t == int(dictValores[f'b{barcoEscolha}'][0])-1:
                                mapaJ[idx][int(barcoPosicao[1]) + t - 1] = '>'
                            else:
                                mapaJ[idx][int(barcoPosicao[1]) + t - 1] = '='
                        break
                    else:
                        print("Posição e/ou direção inválida")
                else:
                    if int(letrasLinhas.index(barcoPosicao[0])) + int(dictValores[f'b{barcoEscolha}'][0]) < 8:
                        for t in range(int(dictValores[f'b{barcoEscolha}'][0])):
                            if t == 0:
                                mapaJ[idx][int(barcoPosicao[1]) - 1] = 'A'
                            elif t == int(dictValores[f'b{barcoEscolha}'][0]) - 1:
                                mapaJ[idx + t][int(barcoPosicao[1]) - 1] = 'V'
                            else:
                                mapaJ[idx + t][int(barcoPosicao[1]) - 1] = 'H'
                        break
                    else:
                        print("Posição e/ou direção inválida")
        barcosUsadosJ.append(barcoEscolha)
    elif barcoEscolha in barcosUsadosJ:
        print('Este barco já foi utilizado')
        escolherBarco()
    printMapa(letrasLinhas, mapaJ)


def colocarBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ):
    cont = 0
    print('Escolha seu barco: ')
    for n in dictValores:
        print(f'{cont+1}. {listaNomes[cont]}, tamanho: {dictValores[n][0]}')
        cont+=1
    escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ)