from random import choice

print('Opções:')
print('0 - Pedra\n1 - Papel\n2 - Tesoura')
jogada = int(input('Escolha sua jogada: '))

if jogada == 0:
    jogada = 'pedra'
elif jogada == 1:
    jogada = 'papel'
elif jogada == 2:
    jogada = 'tesoura'
else:
    jogada = 'invalid'
    print('Jogada inválida!')

pc = choice(['pedra', 'papel', 'tesoura'])

if jogada != 'invalid':
    print('Computador jogou', pc)
    print('Jogador jogou', jogada)
    if (jogada == 'pedra' and pc == 'tesoura') or (jogada == 'papel' and pc == 'pedra') or (jogada == 'tesoura' and pc == 'papel'):
        print('JOGADOR VENCEU')
    elif jogada == pc:
        print('DEU EMPATE')
    else:
        print('COMPUTADOR VENCEU')