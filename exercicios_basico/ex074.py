# Gerando 5 números aleatórios e guardando em uma tupla

from random import randint

conjunto = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for num in conjunto:
    print(f'{num}', end=' ')
print(f'\nO maior valor sorteado foi {max(conjunto)}')
print(f'O menor valor sorteado foi {min(conjunto)}')