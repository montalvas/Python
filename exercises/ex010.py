# Informe um valor em R$  e veja sua conversão em dolar (com cotação atual).

r = float(input('Quanto você tem na carteira R$: '))
d = r / 5.05
print('Com R$ {:.2f} você tem $ {:.2f}.'.format(r, d))
