from time import sleep
from random import randint


itens=('pedra','papel', 'Tesoura')
computador =randint(0,2)
print('''suas opçao:
[ 0 ]pedra
[ 1 ]papel
[ 2 ]tesoura''')

jogador =int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO')
sleep(1)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0: # computador jogou pedra
    if jogador  ==0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
elif computador ==1: #computador jogou papel
    if jogador == 0:
        print('computador venceu')
    elif jogador ==1 :
        print('empate')
    elif jogador == 2:
        print('jogador venceu')
elif computador == 2: # computador jogou tesoura
    if jogador ==0:
        print('jogador venceu')
    elif jogador ==1:
        print('computador venceu')
    elif jogador == 2:
        print('empate ')



