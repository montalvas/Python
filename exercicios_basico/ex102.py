def fatorial(num = 1, show = False):
    '''
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    from time import sleep
    f = 1
    print('-' * 20)
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        print(f'Calculando fatorial de {num}: ', end='')
        for c in range(num, 0, -1):
            f *= c
            if c != 1:
                print(c, end=' x ', flush=True)
            else:
                print(c, end=' = ', flush=True)
            sleep(1)
        return f


print(fatorial(5, True))
print(fatorial(2))
print(fatorial(1))
print(fatorial(10, True))
