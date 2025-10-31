from utilitarios import *

barcosNomes = ['destroyer', 'submarino', 'cruzador', 'couraçado', 'porta-aviões']
barcosValores = {'b1':'22','b2':'33','b3':'33','b4':'44','b5':'55'}
letrasLinhas = ['A','B','C','D','E','F','G','H']
mapaJ1 = [['~']*8 for j in range(8)]
barcosUsadosJ1 = []

printMapa(letrasLinhas, mapaJ1)

for s in range(len(barcosValores)):
    colocarBarco(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJ1, mapaJ1)
printMapa(letrasLinhas, mapaJ1)