# Tabuada 2.0

n = int(input('Tabuada do número: '))

print('{:=^20}'.format(''))
print('{:^20}'.format('TABUADA'))
print('{:=^20}\n'.format(''))

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, c * n))
