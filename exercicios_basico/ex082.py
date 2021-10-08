# Ler valores e separar em par ou impar

par = list()
impar = list()
numeros = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    question = input('Deseja continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
numeros.sort()
for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('-=' * 15)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
