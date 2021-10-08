def pyhelp():
    while True:
        print('~' * 30)
        print('{:^30}'.format('SISTEMA DE AJUDA PYHELP'))
        print('~' * 30)
        comando = input('Função ou Biblioteca > ')
        if comando == 'FIM':
            break
        else:
            help(comando)


pyhelp()