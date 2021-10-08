# Cadastrando usuários

major = 0
men = 0
womanminor = 0

while True:
    print('=' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('=' * 30)
    while True:
        age = int(input('Idade: '))
        if age >= 0:
            break
    while True:
        gender = input('Sexo: [M/F] ')
        if gender in 'fFmM' and gender != '':
            break
    if age > 18:
        major += 1
    if gender in 'mM':
        men += 1
    if age < 20 and gender in 'fF':
        womanminor += 1
    while True:
        question = input('Quer continuar? [S/N] ')
        if question in 'sSnN':
            break
    if question in 'nN':
        break
print('{:=^30}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com mais de 18 anos: {major}')
print(f'Ao todo temos {men} homens cadastrados')
print(f'E temos {womanminor} mulheres com menos de 20 anos.')

