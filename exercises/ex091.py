from random import randint

jogadores = dict()
print('Valores sorteados:')
for c in range(0, 4):
    jogadores[f'jogador{c + 1}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
jogadores = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
print('Ranking dos jogadores:')
for c in range(0, 4):
    print(f'    {c + 1}º lugar: {jogadores[c][0]} com {jogadores[c][1]}')
