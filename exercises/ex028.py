'''
Escreva um programa que faça o pc "pensar" em um número inteiro entre 0 e 5.
Peça para o usuario tentar adivinhar esse número.
Escreva na tela se o usuario acertou ou nao.
'''

from random import randint

rand = randint(0, 5)
print('''Vou pensar em número de 0 a 5...
Tente adivinhar!
...''')
num = int(input('Seu palpite: '))

print('\nSeu número foi: ', num)
print('O computador pensou em: ', rand)
print('Você acertou, parabéns!!' if num == rand else 'Você errou, que pena.')