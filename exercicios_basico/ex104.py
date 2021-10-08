def leiaint(question):
    print('-' * 20)
    while True:
        n = input(question)
        if n.isnumeric() and n != '':
            print(f'Você acabou de digitar o número {n}.')
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


num = leiaint('Digite um número: ')