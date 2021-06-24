# Maior e menor valor e suas poisções em uma lista

numeros = list()
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-' * 25)
print(f'Você digitou os valores {numeros}')
nmax = max(numeros)
nmin = min(numeros)
if numeros.count(nmax) == 1:
    print(f'O maior valor foi {nmax} na posição {numeros.index(nmax)}...')
else:
    print(f'O maior valor foi {nmax} nas posições ', end='')
    for pos, numero in enumerate(numeros):
        if numero == nmax:
            print(pos, end='...')
    print('')
if numeros.count(nmin) == 1:
    print(f'O menor valor foi {nmin} na posição {numeros.index(nmin)}...')
else:
    print(f'O menor valor foi {nmin} nas posições ', end='')
    for pos, numero in enumerate(numeros):
        if numero == nmin:
            print(pos, end='...')