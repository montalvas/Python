def adivinhacao():
    import utils

    utils.mensagem_abertura()
    numero_de_tentativas = utils.escolher_dificuldade()
    numero_sorteado = utils.sortear_numero()
    pontos = 1000
    print('TENTE ACERTAR O NÚMERO SORTEADO!!\n')

    for c in range(1, numero_de_tentativas + 1):
        print(f'Tentativa {c}/{numero_de_tentativas}')
        palpite = int(input('Seu palpite: '))
        res = utils.condicao_vitoria(palpite, numero_sorteado)
        if res:
            break
        else:
            pontos = utils.pontuacao(pontos, palpite, numero_sorteado)
    utils.resultado(numero_sorteado, pontos)