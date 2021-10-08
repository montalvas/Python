# Mostre na tela a sequencia de fibonacci

element = int(input('Quantidade de elementos para mostrar: '))
if element <= 0:
    print('Valor inválido')
else:
    print('Fibonacci: ', end='')
    n1 = 0
    n2 = 1
    if element == 1:
        print(n1, end=' → ')
    elif element == 2:
        print('{} → {}'.format(n1, n2), end=' → ')
    else:
        print('{} → {}'.format(n1, n2), end=' → ')
        c = 2
        while c < element:
            fib = n1 + n2
            print(fib, end=' → ')
            n1 = n2
            n2 = fib
            c += 1
print('FIM')