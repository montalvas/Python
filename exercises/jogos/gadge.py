def mensagem_abertura():
    print('-' * 50)
    print('{:^50}'.format('JOGO DA FORCA'))
    print('-' * 50 + '\n')


def carregar_palavra_secreta():
    from random import choice
    conteudo = []
    try:
        arquivo = open('palavras.txt')
    except FileNotFoundError:
        arquivo = open('palavras.txt', 'w')
    else:
        for linha in arquivo:
            linha = linha.strip()
            conteudo.append(linha)
        arquivo.close()
    palavra = choice(conteudo).upper()
    return palavra


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def palpite(palavra, acertos, tentativas):
    palpite = input('Qual a letra? ').upper()[0]

    if palpite in palavra:
        for c in range(0, len(palavra)):
            if palpite.upper() == palavra[c]:
                acertos[c] = palpite
    else:
        tentativas -= 1
        print('Palpite errado!')
    return tentativas


def mostrar_letras(tentativa, acertos):
    print('-' * 50)
    print(f'Tentativas: {tentativa}')
    print('Palavra: ', end='')
    for letra in acertos:
        print(letra, end=' ')
    print()


def mensagem_vencedor():
    print('Parabéns, você ganhou!')


def mensagem_perdedor(palavra):
    print('Puxa, você foi enforcado!')
    print('A palavra era ', palavra)