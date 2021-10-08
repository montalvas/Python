# Ler o ano de nascimento de 7 pessoas e mostrar quantas são de maior e quantas são de menor idade (21 anos)

year = 2021
adulthood = 0
nonage = 0
for c in range(0, 7):
    age = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c + 1)))
    if year - age >= 21:
        adulthood += 1
    else:
        nonage += 1
print('No total temos {} maioridade e {} menoridade.'.format(adulthood, nonage))