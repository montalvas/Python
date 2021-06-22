# CAIXA ELETRÔNICO

cinquenta = vinte = dez = um = 0

print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)

while True:
    value = int(input('Qual valor você quer sacar? '))
    cinquenta = value // 50
    vinte = (value % 50) // 20
    dez = ((value % 50) % 20) // 10
    um = (((value % 50) % 20) % 10) // 1
    break

print(f'Total de {cinquenta} cédulas de R$ 50,00')
print(f'Total de {vinte} cédulas de R$ 20,00')
print(f'Total de {dez} cédulas de R$ 10,00')
print(f'Total de {um} cédulas de R$ 1,00')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
