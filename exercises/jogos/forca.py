import gadge

def forca():
    gadge.mensagem_abertura()
    acertou = False
    enforcou = False

    palavra_secreta = gadge.carregar_palavra_secreta()
    tentativa = len(palavra_secreta)
    letras_acertadas = gadge.inicializa_letras_acertadas(palavra_secreta)
    gadge.mostrar_letras(tentativa, letras_acertadas)

    while not enforcou and not acertou:
        tentativa = gadge.palpite(palavra_secreta, letras_acertadas, tentativa)
        gadge.mostrar_letras(tentativa, letras_acertadas)

        acertou = '_' not in letras_acertadas
        enforcou = tentativa == 0

    if acertou:
        gadge.mensagem_vencedor()
    else:
        gadge.mensagem_perdedor(palavra_secreta)
    print('FIM DE JOGO')
