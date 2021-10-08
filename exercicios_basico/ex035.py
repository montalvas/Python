# Pode formar um triângulo?

r1 = float(input('Segmento de reta 1: '))
r2 = float(input('Segmento de reta 2: '))
r3 = float(input('Segmento de reta 3: '))

if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            cond = True
        else:
            cond = False
    else:
        cond = False
else:
    cond = False
print('Os 3 segmentos de reta formam um triângulo:', cond)