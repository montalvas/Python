numeros = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-=' * 15)
print(f'O valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')