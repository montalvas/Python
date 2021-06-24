# Cadastrar 5 valores em uma lista e organizar sem usar o Sort()

numeros = list()

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > max(numeros):
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        for p, val in enumerate(numeros):
            if num > val:
                pos = p + 1
            else:
                pos = p
                break
        numeros.insert(pos, num)
        print(f'Adicionado na posição {pos} da lista')
print('-=' * 15)
print(f'O valores digitados foram {numeros}')