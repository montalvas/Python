'''Ler a velocidade de um carro
se ele ultrapassar 80 km/h, ele será multado.
a multa vai custar R$ 7,00 para km acima do limite.'''

v = float(input('Velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('Você ULTRAPASSOU o limite de velocidade! Multa: R$ ', m)