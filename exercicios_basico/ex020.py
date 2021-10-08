# Leia o nome de 4 alunos e sorteie a ordem de apresentação deles.

from random import shuffle

a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')

order = [a1, a2, a3, a4]
shuffle(order)
print('O ordem de apresentação será: ', order)
