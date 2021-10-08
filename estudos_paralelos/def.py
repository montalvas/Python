def mensagem(texto):
    print('-' * 30)
    print('{:^30}'.format(texto))
    print('-' * 30)


mensagem('CURSO EM VIDEO')


def mostrar_nome(nome):
    print(f'Meu nome é {nome}')


mostrar_nome('Lucas')


def contador(*num):
    print(num)


contador(1, 2, 4, 7, 9)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
