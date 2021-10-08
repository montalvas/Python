# Entrar com dois numeros e dizer qual maior ou se são iguais

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print('O maior número é ', n1)
elif n2 > n1:
    print('O maior número é ', n2)
else:
    print('Os dois números são iguais.')