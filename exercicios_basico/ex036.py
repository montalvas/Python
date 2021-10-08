# Empréstimo bancário casa

vhouse = float(input('Informe o valor da casa: '))
sal = float(input('Informe seu salário: '))
time = int(input('Informe o período do financiamento (anos): '))
time *= 12

payment = vhouse / time
if payment <= (sal*0.3):
    print('Serão {} parcelas de R$ {:.2f}'.format(time, payment))
else:
    print('O valor da mensalidade foi superior a 30% do salário.')
