# Loop com números

cond = True
major = minor = media = 0
c = 0
while cond:
    num = int(input('Digite um número: '))
    if c == 0:
        major = minor = num
    else:
        if num > major:
            major = num
        if num < minor:
            minor = num
    c += 1
    media += num
    question = input('Deseja continuar [s/n]: ')
    if question == 'n':
        cond = False
print('O maior número foi', major)
print('O menor número foi', minor)
print('A média entre os {} números digitados foi {:.2f}'.format(c, media / c))