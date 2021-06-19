# Soma entre todos os números impares que são múltiplos de 3 no intervalo entre 1 e 500

s = 0
for c in range(1, 501):
    if  c % 2 == 1 and c % 3 == 0:
        s += c

print('Total:', s)
    