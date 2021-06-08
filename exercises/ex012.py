# Ler o preço de um produto e mostrar seu novo preço com 5% de desconto.

p = float(input('Digite o preço do produto R$: '))
pf = p * 0.95
print('O produto com valor R$ {:.2f} tem 5% de desconto, seu novo valor será R$ {:.2f}'.format(p, pf))
