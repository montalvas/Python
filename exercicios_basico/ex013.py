# Ler o salário de um funcionário e mostrar novo salário com 15% de aumento

name = input('Nome do funcionário: ')
sal = float(input('Salário R$: '))
newsal = sal * 1.15
print('O(A) funcionário(a) {} teve aumento de 15%, seu novo salário será R$ {:.2f}'.format(name, newsal))
