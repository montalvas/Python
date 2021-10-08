from random import randint

guess = list()
print('-' * 25)
print('{:^25}'.format('JOGA NA MEGA SENA'))
print('-' * 25)

while True:
    amount = int(input('Quantos jogos deseja gerar: '))
    if amount > 0:
        break
    else:
        print('Quantidade inválida!')

for c in range(0, amount):
    temp = []
    while len(temp) < 6:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
    temp.sort()
    guess.append(temp[:])
print(f'-=-=-= SORTEANDO {amount} JOGOS -=-=-=')
for i, g in enumerate(guess):
    print(f'Jogo {i + 1}: {g}')
print('-=-=-= < BOA SORTE! > -=-=-=')
