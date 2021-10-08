# Calcular média

n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
med = (n1 + n2)/2
print('Sua média foi:', med)

if med >= 7:
    print('APROVADO')
elif med >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
