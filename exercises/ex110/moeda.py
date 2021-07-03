def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, p):
    r = 1 + (p / 100)
    return n * r


def diminuir(n, p):
    r = 1 - (p / 100)
    return n * r


def resumo(p, a=0, d=0):
    print('-' * 40)
    print('{:^40}'.format('RESUMO DO VALOR'))
    print('-' * 40)
    print('{:<30}'.format('Preço analisado: '), end='')
    print('R$ {}'.format(str(p).replace('.', ',') + '0'))
    print('{:<30}'.format('Dobro do preço: '), end='')
    print('R$ {}'.format(str(dobro(p)).replace('.', ',') + '0'))
    print('{:<30}'.format('Metade do preço: '), end='')
    print('R$ {}'.format(str(metade(p)).replace('.', ',') + '0'))
    print(str(a) + '{:<28}'.format('% de aumento: '), end='')
    print('R$ {}'.format(str(aumentar(p, a)).replace('.', ',') + '0'))
    print(str(d) + '{:<28}'.format('% de redução: '), end='')
    print('R$ {}'.format(str(diminuir(p, d)).replace('.', ',') + '0'))