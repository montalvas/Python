# Leia o nome de 4 alunos e faça um sorteio entre eles.

from random import choice

a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')

escolha = choice([a1, a2, a3, a4])
print('O aluno sorteado foi ', escolha)

