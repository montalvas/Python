# JO KEN PÔ

from random import choice

print('\033[34m{:=^30}'.format('='))
print('\033[33m{:^30}'.format('JO KEN PÔ'))
print('\033[34m{:=^30}\n\033[m'.format('='))
print('\033[33m0 - pedra')
print('\033[34m1 - papel')
print('\033[31m2 - tesoura\033[m\n')
player = int(input('Sua jogada: '))

pc = choice(['pedra', 'papel', 'tesoura'])

if player == 0:
    player = 'pedra'
    if pc == player:
        cond = 'EMPATE'
    elif pc == 'papel':
        cond = 'PERDEU'
    else:
        cond = 'GANHOU'
elif player == 1:
    player = 'papel'
    if pc == player:
        cond = 'EMPATE'
    elif pc == 'tesoura':
        cond = 'PERDEU'
    else:
        cond = 'GANHOU'
elif player == 2:
    player = 'tesoura'
    if pc == player:
        cond = 'EMPATE'
    elif pc == 'pedra':
        cond = 'PERDEU'
    else:
        cond = 'GANHOU'
else:
    cond = 'invalid'
    print('Jogada inválida!')

if cond != 'invalid':
    print('Você jogou:', player)
    print('O pc jogou:', pc)
    print('Resultado: \033[35m{}'.format(cond))


