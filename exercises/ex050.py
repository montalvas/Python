# Ler 6 números inteiros e somar os pares

s = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma entre todos os pares foi:', s)