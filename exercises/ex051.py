# Desenvolva uma PA de 10 termos

p = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão: '))
print('PA: ', end='')
for c in range(0, 10):
    print(p, end=' ')
    p += r