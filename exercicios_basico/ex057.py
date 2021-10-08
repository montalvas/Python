# Verifique a digitação do sexo de uma pessoa

cond = True
while cond:
    gender = input('Digite seu sexo [M/F]: ')
    if gender.islower():
        gender = gender.upper()
    if gender == 'M' or gender == 'F':
        cond = False
print('FIM')