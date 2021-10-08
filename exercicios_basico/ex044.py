# Pagamento de um produto

price = float(input('Digite o preço do produto R$: '))
print('''Como deseja pagar:
0 - À VISTA (MOEDA CORRENTE/CHEQUE) (10% DESCONTO)
1 - À VISTA (CARTÃO) (5% DESCONTO)
2 - 2X NO CARTÃO
3 - 3X OU MAIS NO CARTÃO (20% DE JUROS)
''')
choice = int(input('Opção: '))

if choice == 0:
    finalprice = price * 0.9
elif choice == 1:
    finalprice = price * 0.95
elif choice == 2:
    finalprice = price
elif choice == 3:
    finalprice = price * 1.2
else:
    finalprice = 0
    print('Opção inválida!')

if finalprice != 0:
    print('O total a ser pago será R$ {:.2f}'.format(finalprice))

