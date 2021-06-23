# Tabela campeonato

times = ('Athletico-PR', 'Fortaleza', 'Bragantino', 'Palmeiras', 'Atlético-MG', 'Fluminense', 'Bahia', 'Atlético-GO',
         'Santos', 'Flamengo', 'Corinthians', 'Ceará', 'Internacional', 'Juventude', 'Sport', 'Chapecoense', 'Cuiabá',
         'São Paulo', 'América-MG', 'Grêmio')

print('-=-' * 30)
print(f'Lista de times: {times}')
print('-=-' * 30)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=-' * 30)
print(f'Os quatro últimos são: {times[-1:-5:-1]}')
print('-=-' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 30)
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição")
