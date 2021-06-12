# Leia a distancia da viagem e calcule o valor da passagem

d = float(input('Informe a distância da sua viagem: '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('Para uma viagem de {}, você pagará R$ {:.2f}'.format(d, p))
