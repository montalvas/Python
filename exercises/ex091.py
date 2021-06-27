from random import randint
from time import sleep

jogadores = dict()
print('Valores sorteados:')
for c in range(0, 4):
    jogadores[f'jogador{c + 1}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)
jogadores = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
print('Ranking dos jogadores:')
for k, v in enumerate(jogadores):
    print(f'    {k + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
