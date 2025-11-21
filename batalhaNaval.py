from utilitarios import *

barcosNomes = ['destroyer', 'submarino', 'cruzador', 'couraçado', 'porta-aviões']
barcosValores = {'b1':'22','b2':'33','b3':'33','b4':'44','b5':'55'}
letrasLinhas = ['A','B','C','D','E','F','G','H']
mapaJ1 = [[' .']*8 for j in range(8)]
mapaJ2 = [[' .']*8 for i in range(8)]
barcosUsadosJ1 = []
barcosUsadosJ2 = []
barcosPosJ1 = []
barcosPosJ2 = []
mapaJ = [mapaJ2, mapaJ1]
jogadaJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ1, mapaJ1, 1, barcosPosJ1)
clear_terminal()
input("Press enter to switch players")
jogadaJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ2, mapaJ2, 2, barcosPosJ2)
clear_terminal()

rodada = 1
while inicioRodada(letrasLinhas, mapaJ[rodada], rodada) == 0:
    rodada += 1
    if rodada % 2 != 0:
        inicioRodada(barcosPosJ1, letrasLinhas, mapaJ2, rodada)
    else:
        inicioRodada(barcosPosJ2,letrasLinhas, mapaJ1, rodada)