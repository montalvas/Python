nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')
print('Seja bem-vindo(a), {} {}!'.format(nome, sobrenome))
print('Ordem natural: {0} {1}'.format(nome, sobrenome))
print('Ordem inversa: {1} {0}'.format(nome, sobrenome))
print('Outra forma: {0} {1} {other}'.format(nome, sobrenome, other = 'Santos'))