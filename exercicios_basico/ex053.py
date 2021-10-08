# Leia uma frase e diga se é um palíndromo

print('É UM PALÍNDROMO?')
word = input('Digite a frase: ')

task = word.split()
task = ''.join(task)
inversetask = ''
for c in range(len(task) - 1, -1, -1):
    inversetask += task[c]

if task == inversetask:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')