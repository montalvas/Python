def metade(n, format = False):
    if format:
        return moeda(n / 2)
    else:
        return n / 2


def dobro(n, format = False):
    if format:
        return moeda(n * 2)
    else:
        return n * 2


def aumentar(n, p, format = False):
    r = 1 + (p / 100)
    if format:
        return moeda(n * r)
    else:

        return n * r


def diminuir(n, p, format = False):
    r = 1 - (p / 100)
    if format:
        return moeda(n * r)
    else:
        return n * r


def moeda(p):
    res = str(p).replace('.', ',') + '0'
    return res