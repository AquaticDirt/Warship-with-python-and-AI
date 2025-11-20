import os

def printMapa(letrasLinhas, mapaJ, jogador):
    clear_terminal()
    print(f'  |Mapa do Jogador {jogador}|')
    print('  +-----------------+')
    print('  |', end=' ')
    for num in range(1, len(letrasLinhas) + 1):
        print(num, end=' ')
    print('|')
    print('--+-----------------+')
    for i in range(len(mapaJ)):
        print(*letrasLinhas[i], '|', *mapaJ[i], '|')
    print('--+-----------------+')

def escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador):
    barcoEscolha = input('Sua escolha (1 a 5): ')
    while barcoEscolha not in {'1','2','3','4','5'}:
        barcoEscolha = input('Sua escolha (1 a 5): ')
    escolhaInt = int(barcoEscolha)
    if 1 <= escolhaInt <= 5 and escolhaInt not in barcosUsadosJ:
        while True:
            barcoPosicao = input(f'Escolha uma posição inicial para o seu barco {escolhaInt}. {listaNomes[escolhaInt-1]} (Ex.: D4): ').upper()
            idx = 0
            if barcoPosicao[0] in letrasLinhas:
                while barcoPosicao[0] != letrasLinhas[idx]:
                    idx += 1
            barcoDir = input('Escolha a direção do barco (V para vertical, H para horizontal): ').upper()
            sucesso = False
            if barcoDir == 'H':
                sucesso = barcoDirH(dictValores, barcoPosicao, mapaJ, idx, escolhaInt)
            elif barcoDir == 'V':
                sucesso = barcoDirV(letrasLinhas, dictValores, barcoPosicao, mapaJ, idx, escolhaInt)
            else:
                print("Direção inválida. Use V ou H.")
                continue
            if sucesso:
                barcosUsadosJ.append(escolhaInt)
                break
            else:
                print("Posição inválida ou ocupada! Tente novamente.\n")
    elif escolhaInt in barcosUsadosJ:
        print('Este barco já foi utilizado')
        escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador)
    printMapa(letrasLinhas, mapaJ, jogador)

def barcoDirH(dictValores, barcoPosicao, mapaJ, idx, escolhaInt):
    tamanho = int(dictValores[f'b{escolhaInt}'][0])
    inicio_col = int(barcoPosicao[1]) - 1
    if inicio_col + tamanho > len(mapaJ[idx]):
        return False
    for t in range(tamanho):
        if mapaJ[idx][inicio_col + t] != '~':
            return False
    for t in range(tamanho):
        if t == 0:
            mapaJ[idx][inicio_col] = '<'
        elif t == tamanho - 1:
            mapaJ[idx][inicio_col + t] = '>'
        else:
            mapaJ[idx][inicio_col + t] = '='
    return True

def barcoDirV(letrasLinhas, dictValores, barcoPosicao, mapaJ, idx, escolhaInt):
    tamanho = int(dictValores[f'b{escolhaInt}'][0])
    col = int(barcoPosicao[1]) - 1
    if idx + tamanho > len(letrasLinhas):
        return False
    for t in range(tamanho):
        if mapaJ[idx + t][col] != '~':
            return False
    for t in range(tamanho):
        if t == 0:
            mapaJ[idx][col] = 'A'
        elif t == tamanho - 1:
            mapaJ[idx + t][col] = 'V'
        else:
            mapaJ[idx + t][col] = 'H'
    return True

def colocarBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador):
    cont = 0
    print('Escolha seu barco: ')
    for n in dictValores:
        if cont+1 not in barcosUsadosJ:
            print(f'{cont+1}. {listaNomes[cont]}, tamanho: {dictValores[n][0]}')
        else:
            print(f'{cont + 1}. {listaNomes[cont]}, tamanho: {dictValores[n][0]}   ✅')
        cont += 1
    escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador)

def jogadaJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador):
    printMapa(letrasLinhas, mapaJ, jogador)
    for s in range(len(barcosValores)):
        colocarBarco(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador)
    printMapa(letrasLinhas, mapaJ, jogador)

def ataqueJ(letrasLinhas, jogador, mapaAtacado):
    ataquePos = input('Escolha a posiçao do ataque (Ex.: D4):')
    index = 0
    if ataquePos[0] in letrasLinhas:
        while ataquePos[0] != letrasLinhas[index]:
            index += 1
    if mapaAtacado[index][ataquePos[1]] == '~':
        mapaAtacado[index][ataquePos[1]] = '🌊'
    else:
        mapaAtacado[index][ataquePos[1]] = '💥'
    printMapa(letrasLinhas, mapaAtacado, jogador)

def tem_navios(mapa):
    partes = {"V", "H", "A", "<", ">", "="}
    return any(cell in partes for row in mapa for cell in row)

def inicioRodada(letrasLinhas, mapaAtacado):
    turno = 1
    vitoriaJ = 0
    while vitoriaJ == 0:
        if not tem_navios(mapaAtacado):
            if turno == 1:
                vitoriaJ = 2
            else:
                vitoriaJ = 1
            return vitoriaJ
        else:
            ataqueJ(letrasLinhas, turno, mapaAtacado)
            if turno == 1:
                turno = 2
            else:
                turno = 1
            return vitoriaJ

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')