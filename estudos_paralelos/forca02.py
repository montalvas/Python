print('*' * 50)
print('Bem vindo ao jogo da forca!'.center(50))
print('*' * 50)

palavra_secreta = 'banana'
letras_acertadas = ['_', '_','_', '_', '_', '_']
acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while(not acertou and not enforcou):
    chute = input('Qual a letra? ')

    for letra in palavra_secreta:
        posicao = 0
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra
        else:
            erros += 1
        posicao += 1
    print(letras_acertadas)
    acertou = '_' not in letras_acertadas
    enforcou = erros == 6

if acertou:
    print('VOCÊ GANHOU!')
else:
    print('VOCÊ PERDEU!')
print('FIM DE JOGO!')