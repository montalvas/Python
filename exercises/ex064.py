# Pare com 999

cond = True
sum = 0
amount = 0
while cond:
    num = int(input('Digite um número [999 - stop]: '))
    if num == 999:
        cond = False
    else:
        sum += num
        amount += 1
print('O total de números digitados foi {} e a soma entre eles deu {}'.format(amount, sum))
