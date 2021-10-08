def leiaint(q):
    while True:
        try:
            n = int(input(q))
        except (ValueError, TypeError):
            print('\033[31mNão é um número inteiro\033[m')
        except KeyboardInterrupt:
            print('\033[31mValor não digitado\033[m')
            return 0
        else:
            return n


def leiafloat(q):
    while True:
        try:
            n = float(input(q))
        except (ValueError, TypeError):
            print('\033[31mNão é um número inteiro\033[m')
        except KeyboardInterrupt:
            print('\033[31mValor não digitado\033[m')
            n = 0
            break
        else:
            break
    print(f'O valor real digitado foi {n}')


num = leiaint('Digite um número inteiro: ')
leiafloat('Digite um número real: ')
