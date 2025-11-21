from utilitarios import *
import string

barcosNomes = ['destroyer', 'submarino', 'cruzador', 'couraçado', 'porta-aviões']
barcosValores = {'b1':'22','b2':'33','b3':'33','b4':'44','b5':'55'}
letrasLinhas = list(string.ascii_uppercase[:8])

mapaJ1 = [[' .']*8 for j in range(len(letrasLinhas))]
mapaJ2 = [[' .']*8 for i in range(len(letrasLinhas))]
mapaJs = [mapaJ1, mapaJ2]
barcosUsadosJ1 = []
barcosUsadosJ2 = []
barcosUsadosJs = [barcosUsadosJ1, barcosUsadosJ2]
barcosPosJ1 = []
barcosPosJ2 = []
barcosPosJs = [barcosPosJ1, barcosPosJ2]

inicioJogo(barcosNomes, barcosValores, letrasLinhas, barcosUsadosJs, mapaJs, barcosPosJs)