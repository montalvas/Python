# Ler vários números e pare com 999

amount = 0
sum = 0
while True:
    num = int(input('Digite um número [999 - stop]: '))
    if num == 999:
        break
    else:
        amount += 1
        sum += num
print('A quantidade números digitados foi {}\nA valor total foi {}'.format(amount, sum))