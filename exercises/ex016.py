# Ler um número real e mostrar sua porção inteira

from math import trunc

n = float(input('Informe um número real: '))
print('A porção inteira de {} é {}'.format(n, trunc(n)))
