# Leia um angulo qualquer e calcule seu seno, cosseno e tangente

from math import sin, cos, tan, radians

ang = float(input('Informe um ângulo: '))
angrad = radians(ang)
sen = sin(angrad)
coss = cos(angrad)
tang = tan(angrad)
print('O ângulo {}º tem:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, sen, coss, tang))
