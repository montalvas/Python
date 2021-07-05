def mostrar_dados():
    try:
        arquivo = open('registro.txt', 'r')
    except FileNotFoundError:
        arquivo = open('registro.txt', 'w')
        arquivo.write('-' * 50)
        arquivo.write('\n{:^50}'.format('PESSOAS CADASTRADAS'))
        arquivo.write('\n' + '-' * 50)
        arquivo = open('registro.txt', 'r')
    finally:
        print(arquivo.read())
        arquivo.close()


def novo_registro(nome, idade):
    try:
        arquivo = open('registro.txt', 'a')
    except FileNotFoundError:
        arquivo = open('registro.txt', 'w')
        arquivo.write('-' * 50)
        arquivo.write('\n{:^50}'.format('PESSOAS CADASTRADAS'))
        arquivo.write('\n' + '-' * 50)
        arquivo.close()
    else:
        arquivo.write('\n{:<40}{} anos'.format(nome, idade))
        arquivo.close()


