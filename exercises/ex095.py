time = list()
print('-' * 30)

while True:
    jogador = {'nome': '', 'gols': [], 'total': 0}
    jogador['nome'] = input('Nome: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['total'] += jogador['gols'][c]
    time.append(jogador.copy())
    question = input('Deseja continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
    print('-' * 30)

print('-=' * 25)
print('{:<3} {:<16} {:<16} {:<10}'.format('cod', 'nome', 'gols', 'total'))
print('-' * 50)
for j in time:
    print('{:>3} {:<16} {:<16} {:<10}'.format(time.index(j), j['nome'], str(j['gols']), j['total']))
while True:
    print('-' * 50)
    num = int(input('Mostrar dados de qual jogador? '))
    if 0 <= num <= len(time):
        print(f'-- LEVANTAMENTO DO JOGADOR {time[num]["nome"]}:')
        for c in range(0, len(time[num]['gols'])):
            print(f'No jogo {c + 1} fez {time[num]["gols"][c]} gols.')
    elif num == 999:
        break
    else:
        print(f'ERRO! Não existe jogador com código {num}! Tente novamente')
print('<<< ENCERRANDO >>>')