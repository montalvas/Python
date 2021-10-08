# Adicionando valores a uma lista

numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num in numeros:
        print('Valor duplicado! Não será adicionado...')
    else:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    question = input('Deseja continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
print('-=' * 15)
numeros.sort()
print(f'Você digitou os valores {numeros}')