print('\033[33m{:=^40}'.format(''))
print('\033[31m{:^40}'.format('CONTAGEM REGRESSIVA PARA OS FOGOS'))
print('\033[33m{:=^40}\n'.format(''))
from time import sleep

import emoji

for c in range (10, 0, -1):
    print('\033[31m{}...'.format(c))
    sleep(1)
print(emoji.emojize('\033[m:fireworks: :fireworks: :fireworks: :fireworks: :fireworks:'))
