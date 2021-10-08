# Calcule o fatorial

num = int(input('Digite um número: '))
fat = 1

if num < 1:
    print('O número precisa ser maior ou igual a 1.')
else:
    c = num
    while c != 1:
        fat *= c
        c -= 1
    print('{}! = {}'.format(num, fat))

