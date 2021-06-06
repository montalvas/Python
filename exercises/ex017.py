# Ler o cateto oposto e adjacente de um triangulo retangulo e calcular sua hipotenusa.

from math import sqrt, pow, hypot

co = float((input('Informe o cateto oposto do triângulo retângulo: ')))
ca = float(input('Informe o cateto adjacente do triângulo retângulo: '))

# modo 1:

hip1 = sqrt(pow(co, 2) + pow(ca, 2))

#modo 2:
hip2 = hypot(co, ca)

print('Os catetos {} e {} tem hipotenusa {:.2f}'.format(co, ca, hip2))
