# PA COM WHILE

print('{:=^30}'.format(''))
print('{:^30}'.format('PROGRESSÃO ARITMÉTICA'))
print('{:=^30}\n'.format(''))

pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1

print('PA: ', end='')
while c < 11:
    if c != 10:
        print(pa, end=', ')
    else:
        print(pa)
    pa += r
    c += 1
