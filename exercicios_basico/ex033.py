# Leia 3 números e diga qual o maior e o menor

print('Informe 3 números\n')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 == n2 == n3:
    bigger = n1
    smaller = n1
elif n1 > n2 and n1 > n3:
    bigger = n1
    if n2 > n3:
        smaller = n3
    else:
        smaller = n2
elif n2 > n1 and n2 > n3:
    bigger = n2
    if n1 > n3:
        smaller = n3
    else:
        smaller = n1
else:
    bigger = n3
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
print('O maior número foi: {}\nO menor número foi {}'.format(bigger, smaller))