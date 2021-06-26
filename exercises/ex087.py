matriz = [[], [], []]
somapar = somatercol = maiorseg = 0

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {i}]: ')))
print('-=' * 20)
for c in range(0, 3):
    for i in range(0, 3):
        if matriz[c][i] % 2 == 0:
            somapar += matriz[c][i]
        if i == 2:
            somatercol += matriz[c][i]
        if c == 1 and matriz[c][i] > maiorseg:
            maiorseg = matriz[c][i]
        print(f'[ {matriz[c][i]} ]', end='')
    print('')
print('-=' * 20)
print(f'A soma de todos os pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somatercol}')
print(f'O maior valor da segunda linha foi {maiorseg}')