# Identificar se um número é primo ou não

print('É PRIMO?')
num = int(input('Informe o número: '))

totdiv = 0
if num <= 1:
    print('NÃO É PRIMO!')
else:
    for c in range(1, num + 1):
        if num % c == 0:
            totdiv += 1
    if totdiv == 2:
        print('{} é primo!'.format(num))
    else:
        print('{} não é primo!'.format(num))