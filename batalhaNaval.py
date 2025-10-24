"""
__     __                  __
\ \ _ / / __  ____   ____ | |     __  ___  ____
 \ V V / //\\ | D ) ( __/ | '--, | | | D_)( __/
  \_^_/ /_/\_\|_A_\ \==_) |_||_| |_| |_|  \==_)

Regras:
   1. existem 5 barcos a serem posicionados:
       * destroyer
       * submarino
       * cruzador
       * couraçado
       * porta-aviões
   2. os barcos posicionados devem estar contidos dentro da matriz 8x8, não podem conter duplicatas e não podem se sobrepor
   3. os tabuleiros de cada jogador deve ser secreto ao seu oponente
   4. as rodadas devem ser alternadas, jogador 1 dá seu palpite, depois jogador 2 e assim por diante
   5. ganha o jogador que afundar todos os navios do oponente
"""
barcosNomes = ['destroyer', 'submarino', 'cruzador', 'couraçado', 'porta-aviões']
barcosValores = {'b1':'22','b2':'33','b3':'33','b4':'44','b5':'55'}
letrasLinhas = ['A','B','C','D','E','F','G','H']
mapaJ1 = [['~']*8 for j in range(8)]
barcosUsadosJ1 = []
def printMapa():
   print('  |', end= ' ')
   for num in range(1, len(letrasLinhas) + 1):
       print(num, end= ' ')
   print('|')
   print('--+-----------------+')
   for i in range(len(mapaJ1)):
       print(*letrasLinhas[i],'|',*mapaJ1[i],'|')
   print('--+-----------------+')
printMapa()


def colocarBarco():
   cont = 0
   print('Escolha seu barco: ')
   for n in barcosValores:
       print(f'{cont+1}. {barcosNomes[cont]}, tamanho: {barcosValores[n][0]}')
       cont+=1
   def escolherBarco():
       barcoEscolha = int(input('Sua escolha (1 a 5): '))
       if 1 <= barcoEscolha <= 5 and barcoEscolha not in barcosUsadosJ1:
           while True:
               barcoPosicao = (input(f'Escolha uma posição inicial para o seu barco: {barcoEscolha}. {barcosNomes[barcoEscolha-1]} (Ex.: D4): ')).upper()
               idx = 0
               if barcoPosicao[0] in letrasLinhas:
                   while barcoPosicao[0] != letrasLinhas[idx]:
                       idx+=1
               barcoDir = input('Escolha a direção do barco (V para vertical, H para horizontal): ').upper()
               if barcoDir=='V' or barcoDir=='H':
                   if barcoDir=='H':
                       if int(barcoPosicao[1]) + int(barcosValores[f'b{barcoEscolha}'][0]) < 8:
                           for t in range(int(barcosValores[f'b{barcoEscolha}'][0])):
                               if t == 0:
                                   mapaJ1[idx][int(barcoPosicao[1])-1] = '<'
                               elif t == int(barcosValores[f'b{barcoEscolha}'][0])-1:
                                   mapaJ1[idx][int(barcoPosicao[1]) + t - 1] = '>'
                               else:
                                   mapaJ1[idx][int(barcoPosicao[1]) + t - 1] = '='
                           break
                       else:
                           print("Posição e/ou direção inválida")
                   else:
                       if int(letrasLinhas.index(barcoPosicao[0])) + int(barcosValores[f'b{barcoEscolha}'][0]) < 8:
                           for t in range(int(barcosValores[f'b{barcoEscolha}'][0])):
                               if t == 0:
                                   mapaJ1[idx][int(barcoPosicao[1]) - 1] = 'A'
                               elif t == int(barcosValores[f'b{barcoEscolha}'][0]) - 1:
                                   mapaJ1[idx + t][int(barcoPosicao[1]) - 1] = 'V'
                               else:
                                   mapaJ1[idx + t][int(barcoPosicao[1]) - 1] = 'H'
                           break
                       else:
                           print("Posição e/ou direção inválida")
           barcosUsadosJ1.append(barcoEscolha)
       elif barcoEscolha in barcosUsadosJ1:
           print('Este barco já foi utilizado')
           escolherBarco()
   escolherBarco()


   printMapa()
for s in range(len(barcosValores)):
   colocarBarco()