# matriz 3x3

matriz = [[], [], []]

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {i}]: ')))
print('-=' * 15)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]} ]', end='')
    print('')