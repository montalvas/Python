def mensagem_abertura():
    print('''Escolha um nível:
        [1] - 20 tentativas
        [2] - 10 tentativas
        [3] - 05 tentativas''')


def escolher_dificuldade():
    dificuldade = int(input('Escolha: '))
    if dificuldade == 1:
        numero_de_tentativas = 20
    elif dificuldade == 2:
        numero_de_tentativas = 10
    elif dificuldade == 3:
        numero_de_tentativas = 5
    else:
        numero_de_tentativas = 20
    return numero_de_tentativas


def sortear_numero():
    from random import randint
    numero = randint(1, 100)
    return numero


def condicao_vitoria(palpite, numero_sorteado):
    ganhar = palpite == numero_sorteado
    if ganhar:
        print(f'Você acertou!!')
        return True
    return False


def pontuacao(pontos, palpite, numero_sorteado):
    maior = palpite > numero_sorteado
    menor = palpite < numero_sorteado
    if maior:
        print('Você errou! palpite maior que o número sorteado')
        pontos -= (palpite - numero_sorteado)
    elif menor:
        print('Você errou! palpite menor que o número sorteado')
        pontos -= (numero_sorteado - palpite)
    return pontos


def resultado(numero_sorteado, pontos):
    print(f'Você acertou o número {numero_sorteado}!!')
    print(f'Você fez {pontos} pontos.')