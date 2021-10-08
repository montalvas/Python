# Idade para alistamento

print('''===============================
     ALISTAMENTO MILITAR
===============================
''')
age = int(input('Digite sua idade: '))
if age == 18:
    print('Você tem {}, está no tempo de se alistar!'.format(age))
elif age > 18:
    dif = age - 18
    print('Você deveria ter se alistado a {} anos!'.format(dif))
else:
    dif = 18 - age
    print('Você ainda é menor de idade! Volte daqui a {} anos.'.format(dif))
