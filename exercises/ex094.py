pessoas = list()
pessoa = {'nome': '', 'idade': 0, 'sexo': ''}
media = 0

while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        idade = int(input('Idade: '))
        if idade >= 0:
            pessoa['idade'] = idade
            media += idade
            break
        else:
            print('Idade inválida, digite novamente.')
    while True:
        sexo = input('Sexo [M/F]: ').upper()
        if sexo in 'MF' and sexo != '':
            pessoa['sexo'] = sexo
            break
        else:
            print('Sexo inválido, digite novamente.')
    pessoas.append(pessoa.copy())
    question = input('Quer continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
media = media / len(pessoas)
print('-=' * 25)
print(f'O grupo tem {len(pessoas)} pessoas.')
print('-' * 40)
mulheres = list()
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
print(f'A média de idade do grupo é de {media} anos.')
print('-' * 40)
print('As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m, end=' ')
print()
print('-' * 40)
print('A lista de pessoas com idade acima da média é:')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print('\n')
print('<<< ENCERRADO >>>')