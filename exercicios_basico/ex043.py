# Cálculo IMC

weight = float(input('Informe seu peso: '))
height = float(input('Informe sua altura: '))
imc = weight / (height * height)
print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')