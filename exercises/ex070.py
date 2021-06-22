# Cadastro de produtos

total = morethanthousand = temp = 0
cheaper = ''
cond = True

print('=' * 30)
print('{:^30}'.format('MERCADÃO'))
print('=' * 30)

while cond:
    product = input('Digite o nome do produto: ')
    while True:
        price = float(input('Digite o preço do produto: '))
        if price >= 0:
            if price > 1000:
                morethanthousand += 1
            break
    if temp == 0:
        temp = price
        cheaper = product
    else:
        if price < temp:
            temp = price
            cheaper = product
    total += price
    while True:
        question = input('Deseja continuar? [S/N] ')
        if question in 'sS':
            break
        elif question in 'nN':
            cond = False
            break
print('=' * 20)
print('{:^20}'.format('TOTAL'))
print('=' * 20)
print('Total das compras R$ {:.2f}'.format(total))
print(f'Foram comprados {morethanthousand} produtos acima de R$ 1.000,00')
print('O produto mais barato foi {} que custou R$ {:.2f}'.format(cheaper, temp))
