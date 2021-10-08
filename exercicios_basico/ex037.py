# Converta um número para outras bases

num = int(input('Informe um número: '))
print('''Escolha a base para conversão:
1 - binário
2 - octal
3 - hexadecimal
''')
choice = int(input('Escolha: '))

if choice == 1:
    convnum = format(num, 'b')
    print('O número {} convertido p/ binário é: {}'.format(num, convnum))
elif choice == 2:
    convnum = format(num, 'o')
    print('O número {} convertido p/ octal é: {}'.format(num, convnum))
elif choice == 3:
    convnum = format(num, 'x')
    print('O número {} convertido p/ hexadecimal é: {}'.format(num, convnum))
else:
    print('Opção inválida!')
