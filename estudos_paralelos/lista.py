lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
lista_ordenada = sorted(lista)
media = 0
soma_negativos = 0

print(f'Maior elemento: {max(lista)}')
print(f'Menor elemento: {min(lista)}')
print('Números pares: ', end='')
for numero in lista_ordenada:
    if numero % 2 == 0:
        media += numero
        print(numero, end=' ')
    else:
        media += numero
    if numero < 0:
        soma_negativos += numero
print(f'\nO número {lista[0]} aparece {lista.count(lista[0])} vezes')
media = media/len(lista)
print('A média dos elementos é {:.2f}'.format(media))
print(f'A soma entre os números negativos é {soma_negativos}')
