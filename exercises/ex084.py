pessoas = list()
pessoa = list()
bigger = lower = 0

while True:
    pessoa.append(input('Digite o nome: '))
    pessoa.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        bigger = lower = pessoa[1]
    else:
        if pessoa[1] > bigger:
            bigger = pessoa[1]
        if pessoa[1] < lower:
            lower = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    question = input('Deseja continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
print('-=' * 15)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('O maior peso foi de {:.1f}Kg. Peso de '.format(bigger), end='')
for p in pessoas:
    if p[1] == bigger:
        print(f'[{p[0]}]', end=' ')
print('\nO menor peso foi de {:.1f}Kg. Peso de '.format(lower), end='')
for p in pessoas:
    if p[1] == lower:
        print(f'[{p[0]}]', end=' ')