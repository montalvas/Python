# Ler dois valores e mostrar um menu na tela

cond = True

print('\033[33m{:=^20}'.format(''))
print('{:^20}'.format('CALCULADORA'))
print('{:=^20}\033[m\n'.format(''))

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while cond:
    print('''\nMENU:
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair''')

    choice = int(input('Escolha: '))
    if choice == 1:
        print('O resultado entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif choice == 2:
        print('O resultado entre {} x {} = {}'.format(n1, n2, n1 * n2))
    elif choice == 3:
        if n1 > n2:
            print('O maior número é', n1)
        elif n2 > n2:
            print('O maior número é', n2)
        else:
            print('O números são iguais.')
    elif choice == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif choice == 5:
        print('ENCERRANDO...')
        cond = False
    else:
        print('Opção inválida!')