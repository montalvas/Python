# Acerte o número!

print('\033[33m{:=^30}'.format(''))
print('{:^30}'.format('ACERTE O NÚMERO!'))
print('{:=^30}\033[m\n'.format(''))

from random import randint

print('O computador pensou em um número entre 0 e 10... tente adivinhar!')
randnum = randint(0, 10)
attempts = 0

while True:
    guess = int(input('Palpite: '))
    if guess == randnum:
        attempts += 1
        break
    else:
        attempts += 1
print('Você acertou! O número foi: \033[34m{}\033[m'.format(guess))
print('O número de tentativas foi: \033[31m{}\033[m'.format(attempts))