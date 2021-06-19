# Lidando com várias informações

media = 0
maioridade = 0
homemvelho = 'nenhum'
menorvinte = 0

for c in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo(M/F): ')
    print('=======================')

    media += idade

    if sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            homemvelho = nome
    else:
        if idade < 20:
            menorvinte += 1

print('A média de idade é {:.2f}'.format(media / 4))
print('O homem mais velho é ', homemvelho)
print('A quantidade de mulheres com menos de vinte anos é ', menorvinte)
