# Acerte o número!

print('\033[33m{:=^30}'.format(''))
print('{:^30}'.format('ACERTE O NÚMERO!'))
print('{:=^30}\033[m\n'.format(''))

from random import randint

print('O computador pensou em um número entre 0 e 10... tente adivinhar!')
randnum = randint(0, 10)
attempts = 0
cond = True

while cond:
    guess = int(input('Palpite: '))
    attempts += 1
    if guess == randnum:
        cond = False
    elif guess > randnum:
        print('Menos... tente novamente.')
    else:
        print('Mais... tente novamente.')
print('Você acertou! O número foi: \033[34m{}\033[m'.format(guess))
print('O número de tentativas foi: \033[31m{}\033[m'.format(attempts))