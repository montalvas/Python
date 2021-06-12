# Receba um salário e calcule seu aumento

sal = float(input('Informe o salário: '))
if sal > 1250:
    sal *= 1.1
else:
    sal *= 1.15
print('Seu novo salário é R$ {:.2f}'.format(sal))
