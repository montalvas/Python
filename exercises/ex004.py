# Leia algo digitado, diga o tipo primitivo e as possívesi informações

value = input('Digite algo: ')
print('O tipo primitivo de {} é: {}'.format(value, type(value)))
print('É numérico: {}'.format(value.isnumeric()))
print('É alfabético: {}'.format(value.isalpha()))
print('É alfanumérico: {}'.format(value.isalnum()))
print('É decimal: {}'.format(value.isdecimal()))
print('É composto por espaços em branco: {}'.format(value.isspace()))
print('É composto por dígitos: {}'.format(value.isdigit()))
print('Está todo em maiúsculo: {}'.format(value.isupper()))
print('Está todo em minúsculo: {}'.format(value.islower()))
print('Está capitalizado: {}'.format(value.istitle()))
