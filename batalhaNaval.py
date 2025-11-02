from utilitarios import *

barcosNomes = ['destroyer', 'submarino', 'cruzador', 'couraçado', 'porta-aviões']
barcosValores = {'b1':'22','b2':'33','b3':'33','b4':'44','b5':'55'}
letrasLinhas = ['A','B','C','D','E','F','G','H']
mapaJ1 = [['~']*8 for j in range(8)]
mapaJ2 = [['~']*8 for i in range(8)]
barcosUsadosJ1 = []
barcosUsadosJ2 = []

jogadaJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ1, mapaJ1, 1)
jogadaJ(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ2, mapaJ2, 2)


