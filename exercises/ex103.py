def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 20)
nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric and gols != '':
    gols = int(gols)
else:
    gols = 0
if nome != '':
    ficha(nome, gols)
else:
    ficha(gols=gols)