import os

def printMapa(letrasLinhas, mapaJ, jogador):
    clear_terminal()
    print(f'  |     Mapa do Jogador {jogador}    |')
    print('--+--------------------------+')
    print('  |', end='  ')
    for num in range(1, len(letrasLinhas) + 1):
        print(num, end='  ')
    print('|')
    print('--+--------------------------+')
    for i in range(len(mapaJ)):
        print(*letrasLinhas[i], '|', *mapaJ[i], ' |')
    print('--+--------------------------+')

def escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador, barcosPosJ):
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
                sucesso = barcoDirH(dictValores, barcoPosicao, mapaJ, idx, escolhaInt, barcosPosJ, letrasLinhas)
            elif barcoDir == 'V':
                sucesso = barcoDirV(letrasLinhas, dictValores, barcoPosicao, mapaJ, idx, escolhaInt, barcosPosJ)
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
        escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador, barcosPosJ)
    printMapa(letrasLinhas, mapaJ, jogador)

def barcoDirH(dictValores, barcoPosicao, mapaJ, idx, escolhaInt, barcosPosJ, letrasLinhas):
    tamanho = int(dictValores[f'b{escolhaInt}'][0])
    col = int(barcoPosicao[1]) - 1
    if col + tamanho > len(mapaJ[idx]):
        return False
    for t in range(tamanho):
        if mapaJ[idx][col + t] != ' .':
            return False
    for t in range(tamanho):
        if t == 0:
            mapaJ[idx][col] = ' <'
            barcosPosJ[escolhaInt] = f'{letrasLinhas[idx]}{col+1}'
        elif t == tamanho - 1:
            mapaJ[idx][col + t] = ' >'
            barcosPosJ[escolhaInt] = f'{barcosPosJ[escolhaInt]},{letrasLinhas[idx]}{col+1+t}'
        else:
            mapaJ[idx][col + t] = ' ='
            barcosPosJ[escolhaInt] = f'{barcosPosJ[escolhaInt]},{letrasLinhas[idx]}{col+1+t}'
    return True

def barcoDirV(letrasLinhas, dictValores, barcoPosicao, mapaJ, idx, escolhaInt, barcosPosJ):
    tamanho = int(dictValores[f'b{escolhaInt}'][0])
    col = int(barcoPosicao[1]) - 1
    if idx + tamanho > len(letrasLinhas):
        return False
    for t in range(tamanho):
        if mapaJ[idx + t][col] != ' .':
            return False
    for t in range(tamanho):
        if t == 0:
            mapaJ[idx][col] = ' A'
            barcosPosJ[escolhaInt] = f'{letrasLinhas[idx]}{col+1}'
        elif t == tamanho - 1:
            mapaJ[idx + t][col] = ' V'
            barcosPosJ[escolhaInt] = f'{barcosPosJ[escolhaInt]},{letrasLinhas[idx+t]}{col+1}'
        else:
            mapaJ[idx + t][col] = ' H'
            barcosPosJ[escolhaInt] = f'{barcosPosJ[escolhaInt]},{letrasLinhas[idx+t]}{col+1}'

    return True

def colocarBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador, barcosPosJ):
    cont = 0
    print('Escolha seu barco: ')
    for n in dictValores:
        if cont+1 not in barcosUsadosJ:
            print(f'{cont+1}. {listaNomes[cont]}, tamanho: {dictValores[n][0]}')
        else:
            print(f'{cont + 1}. {listaNomes[cont]}, tamanho: {dictValores[n][0]}   ✅')
        cont += 1
    escolherBarco(listaNomes, dictValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador, barcosPosJ)

def setupJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador, barcosPosJ):
    printMapa(letrasLinhas, mapaJ, jogador)
    for s in range(len(barcosValores)):
        colocarBarco(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ, mapaJ, jogador, barcosPosJ)

def inicioJogo(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJs, mapaJs, mapaJsOculto, barcosPosJs):
    setupJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJs[0], mapaJs[0], 1, barcosPosJs[0])
    clear_terminal()
    input("Press enter to switch players")
    setupJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJs[1], mapaJs[1], 2, barcosPosJs[1])
    clear_terminal()
    input("Press enter to start game")
    rodada = 1
    while True:
        modRodada = rodada %2
        input("press enter to change players")
        if modRodada != 0:
            vitoriaJ = inicioRodada(letrasLinhas, barcosPosJs[modRodada], mapaJs[modRodada], mapaJsOculto[modRodada], modRodada + 1, mapaJs[0], modRodada)
        else:
            vitoriaJ = inicioRodada(letrasLinhas, barcosPosJs[modRodada], mapaJs[modRodada], mapaJsOculto[modRodada], modRodada + 1, mapaJs[1], modRodada + 2)
        rodada += 1
        if vitoriaJ == 1:
            print(f"Jogador {vitoriaJ} venceu!!")
            break
        elif vitoriaJ == 2:
            print(f"Jogador {vitoriaJ} venceu!!")
            break
    return

def tem_navios(mapaJ):
    partes = {" V", " H", " A", " <", " >", " ="}
    return any(cell in partes for row in mapaJ for cell in row)

def inicioRodada(letrasLinhas, barcosPosJ, mapaAtacado, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante):
    vitoriaJ = 0
    while vitoriaJ == 0:
        if not tem_navios(mapaAtacado):
            if jogadorAtacante == 1:
                vitoriaJ = 2
            else:
                vitoriaJ = 1
            return vitoriaJ
        else:
            ataqueJ(barcosPosJ, letrasLinhas, mapaAtacado, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante)
            input("press enter to change players")
            clear_terminal()
            return vitoriaJ

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printMapaDuplo(letrasLinhas, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante):
    clear_terminal()
    clear_terminal()
    print(f'  |     Mapa do Jogador {jogadorAtacado}    |')
    print('  |', end='  ')
    for num in range(1, len(letrasLinhas) + 1):
        print(num, end='  ')
    print('|')
    print('--+--------------------------+')
    for i in range(len(mapaAtacadoOculto)):
        print(*letrasLinhas[i], '|', *mapaAtacadoOculto[i], ' |')
    print('--+--------------------------+')
    print(f'  |     Mapa do Jogador {jogadorAtacante}    |')
    print('  |', end='  ')
    for num in range(1, len(letrasLinhas) + 1):
        print(num, end='  ')
    print('|')
    print('--+--------------------------+')
    for i in range(len(mapaAtacante)):
        print(*letrasLinhas[i], '|', *mapaAtacante[i], ' |')

def ataqueJ(barcosPosJ, letrasLinhas, mapaAtacado, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante):
    printMapaDuplo(letrasLinhas, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante)
    ataquePos = input('Escolha a posiçao do ataque (Ex.: D4): ')
    idx = 0
    col = int(ataquePos[1]) - 1
    if ataquePos[0].upper() in letrasLinhas and col <= 7:
        while ataquePos[0].upper() != letrasLinhas[idx]:
            idx += 1
    else:
        print('Posição inválida, tente novamente')
        ataqueJ(barcosPosJ, letrasLinhas, mapaAtacado, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante)
    if mapaAtacadoOculto[idx][col] in ['💥', '🌊']:
        ataqueJ(barcosPosJ, letrasLinhas, mapaAtacado, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante)
    for key, value in barcosPosJ.items():
        if ataquePos.upper() in value:
            inBarcosPosJ = True
            mapaAtacadoOculto[idx][col] = '💥'
            mapaAtacado[idx][col] = '💥'
            temp_list = value.split(',')
            temp_list.remove(ataquePos.upper())
            temp = ''
            for i in range(len(temp_list)):
                if (i == len(temp_list) - 1):
                    temp += str(temp_list[i])
                else:
                    temp += str(temp_list[i])+','
            barcosPosJ[key] = temp
            if (len(barcosPosJ[key]) == 0):
                print(f"\n\n\n NAVIO {key} AFUNDADO \n\n\n")
            break
        else:
            inBarcosPosJ = False
    if inBarcosPosJ == False:
        mapaAtacadoOculto[idx][col] = '🌊'
        mapaAtacado[idx][col] = '🌊'
    printMapaDuplo(letrasLinhas, mapaAtacadoOculto, jogadorAtacado, mapaAtacante, jogadorAtacante)