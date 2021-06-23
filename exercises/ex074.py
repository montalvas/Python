# Gerando 5 números aleatórios e guardando em uma tupla

from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)

tupla = tuple((n1, n2, n3, n4, n5))
print('Os valores sorteados foram: ', end='')
for num in tupla:
    print(f'{num}', end=' ')
print(f'\nO maior valor sorteado foi {sorted(tupla)[4]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')