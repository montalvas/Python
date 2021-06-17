# CATEGORIA ATLETA

age = int(input('Informe sua idade: '))

if age <= 9:
    print('Categoria: MIRIM')
elif age <= 14:
    print('Categoria: INFANTIL')
elif age <= 19:
    print('Categoria: JUNIOR')
elif age <= 20:
    print('Categoria: SENIOR')
else:
    print('MASTER')
