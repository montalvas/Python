# PA COM WHILE

print('{:=^30}'.format(''))
print('{:^30}'.format('PROGRESSÃO ARITMÉTICA'))
print('{:=^30}\n'.format(''))

pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = n = 1
lim = 11
amount = 10

while n != 0:
    print('\nPA: ', end='')
    while c < lim:
        if c != (lim - 1):
            print(pa, end=', ')
        else:
            print(pa)
        pa += r
        c += 1
    n = int(input('Quer mostrar mais termos?\n[0 - Não] ou [Digite]: '))
    if n == 0:
        print('FIM...')
    else:
        lim += n
        amount += n
print('Foram mostrados {} termos.'.format(amount))
