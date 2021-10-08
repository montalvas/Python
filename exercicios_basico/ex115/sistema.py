import arquivos


def titulo(msg):
    print('-' * 50)
    print('{:^50}'.format(msg))
    print('-' * 50)


def iniciar():
    while True:
        titulo('MENU PRINCIPAL')
        print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m')
        print('\033[33m2 -\033[m \033[34mCadastrar nova pessoa\033[m')
        print('\033[33m3 -\033[m \033[34mSair do sistema\033[m')
        print('-' * 50)
        while True:
            try:
                option = int(input('\033[33mSua opção:\033[m '))
            except (ValueError, TypeError):
                print('\033[31mOpção inválida, digite novamente!\033[m')
            else:
                if 0 < option < 4:
                    break
                else:
                    print('\033[31mOpção inválida, digite novamente!\033[m')
        if option == 1:
            arquivos.mostrar_dados()
        elif option == 2:
            while True:
                titulo('NOVO CADASTRADO')
                while True:
                    nome = input('Nome: ').strip()
                    if nome.isnumeric() or nome == '' or nome.isalnum():
                        print('\033[31mErro: nome inválido!\033[m')
                    else:
                        break
                while True:
                    try:
                        idade = int(input('Digite sua idade: '))
                    except (ValueError, TypeError):
                        print('\033[31mErro: digite um número inteiro válido!\033[m')
                    else:
                        break
                arquivos.novo_registro(nome, idade)
                print(f'Novo registro de {nome} adicionado.')
                break
        elif option == 3:
            print('\033[34mENCERRANDO O SISTEMA\033[33m...\033[m')
            break