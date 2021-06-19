# Ler o peso de 5 pessoas e definir qual o maior e qual o menor.

maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if c == 0:
        menor = peso
    else:
        if peso < menor:
            menor = peso
print('O maior peso foi: {} KG'.format(maior))
print('O menor peso foi: {} KG'.format(menor))