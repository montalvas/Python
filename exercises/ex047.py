#Todos os números pares entre 1 e 50

print('TODOS OS PARES ENTRE 1 E 50:')
for c in range(1, 51):
    if c % 2 == 0:
        print('\033[34m{}\033[m'.format(c), end=' ')