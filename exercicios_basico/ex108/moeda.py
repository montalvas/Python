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


def moeda(p):
    res = str(p).replace('.', ',') + '0'
    return res