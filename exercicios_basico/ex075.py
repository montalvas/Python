# Analisando números

conjunto = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))

print(f'Os números digitados foram: {conjunto}')
print(f'O valor 9 apareceu {conjunto.count(9)} vezes')
if conjunto.count(3) != 0:
    print(f'O valor 3 apareceu na {conjunto.index(3) + 1}ª posição')
else:
    print('O valor 3 não apareceu em nenhum posição.')
print('Os valores pares digitados foram: ', end='')
for num in conjunto:
    if num % 2 == 0:
        print(num, end=' ')