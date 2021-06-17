# 3 segmentos formam um triângulo? qual triângulo eles formam?

seg1 = int(input('Valor do 1º segmento: '))
seg2 = int(input('Valor do 2ª segmento: '))
seg3 = int(input('Valor do 3ª segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 == seg3:
        tipo = 'Equilátero'
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print('Os segmentos formam um triângulo {}'.format(tipo))
else:
    print('Os segmentos não formam um triângulo!')
