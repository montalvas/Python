jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
jogador['gols'] = list()
jogador['total'] = 0
for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}: ')))
    jogador['total'] += jogador['gols'][c]
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
