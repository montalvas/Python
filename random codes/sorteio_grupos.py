from random import sample

alunos = 25
numeros = []
for c in range(1, alunos + 1):
    numeros.append(c)

grupos = []

while len(numeros) != 0:
    if len(numeros) >=4:
        grupo = sample(numeros, k=4)
    else:
        grupo = numeros.copy()
    grupos.append(grupo)
    for num in grupo:
        numeros.remove(num)

for grupo in grupos:
    print(grupo)