# Jogar Par ou Impar

from random import randint
wins = 0

while True:
    print('-=-' * 10)
    print('VAMOS JOGAR \033[34mPAR\033[m OU \033[31mIMPAR\033[m')
    print('-=-' * 10)
    num = int(input('Digite um valor: '))
    choice = input('Par ou Impar? [P/I] ')[0]
    pc = randint(0, 10)
    total = num + pc
    print(f'O computador jogou {pc}')
    if total % 2 == 0:
        print(f'O total foi {total}, deu \033[34mPAR\033[m')
        if choice in 'pP':
            print('O jogador ganhou!')
            wins += 1
        else:
            print('O computador ganhou!')
            break
    else:
        print(f'O total foi {total}, deu \033[31mIMPAR\033[m')
        if choice in 'iI':
            print('O jogador venceu!')
            wins += 1
        else:
            print('O computador venceu!')
            break
print(f'FIM DE JOGO! Você ganhou {wins} vezes.')