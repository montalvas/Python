# Listagem de preços

produtos = ('Processador Ryzen 5600x', 1829.90, 'Teclado T-Dagger Bora Single', 176.90,
            'Monitor Gamer Samsung 27 Curvo', 2499.90, 'Impressora 3D Creality', 1799.90,
            'Mouse Gamer Redragon Cobra', 109.90)

print('=' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('=' * 50)
for produto in produtos:
    if produtos.index(produto) % 2 == 0:
        print('{:.<38}'.format(produto), end='R$')
    else:
        print('{:>10.2f}'.format(produto))
print('=' * 50)