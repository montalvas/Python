# Tabuada de diversos números

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    else:
        c = 1
        print('-' * 30)
        while c <= 10:
            print(f'{num} x {c} = {num * c}')
            c += 1
        print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')