import forca
import adivinhacao

while True:
    print('-' * 30)
    print('{:^30}'.format('MENU DE JOGOS'))
    print('-' * 30)
    print('1. Adivinhação')
    print('2. Forca')
    print('3. Sair')
    while True:
        try:
            escolha = int(input('Qual jogo quer jogar? Digite o número: '))
        except (TypeError, ValueError):
            print('Opção inválida')
        else:
            print()
            break
    if escolha == 1:
        adivinhacao.adivinhacao()
    elif escolha == 2:
        forca.forca()
    elif escolha == 3:
        break
    else:
        print('Opção inválida')