# Varrendo uma lista de números

numeros = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    question = input('Deseja continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
print('-=' * 15)
print(f'A quantidade de números digitados foi {len(numeros)}')
numeros.sort(reverse=True)
print(f'A lista em ordem descrente é {numeros}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista! na posição {numeros.index(5)}')
else:
    print('O valor 5 não faz parte da lista!')