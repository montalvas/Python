# Analisando números

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla = tuple((n1, n2, n3, n4))

print(f'Os números digitados foram: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) != 0:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não apareceu em nenhum posição.')
print('Os valores pares digitados foram: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')