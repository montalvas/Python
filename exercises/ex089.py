alunos = list()

while True:
    aluno = []
    aluno.append(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    aluno.append([n1, n2])
    aluno.append((n1 + n2)/2)
    alunos.append(aluno[:])
    question = input('Deseja continuar? [S/N] ')
    if question in 'nN' and question != '':
        break
print('-=' * 20)
print('No. NOME               MÉDIA')
print('-' * 35)
for p, a in enumerate(alunos):
    print('{:<3} {:<20} {:>3.1f}'.format(p, a[0], a[2]))
print('-' * 35)
while True:
    option = int(input('Mostrar notas de qual aluno: (999 interrompe): '))
    if option == 999:
        break
    else:
        if 0 <= option < len(alunos):
            print(f'Notas de {alunos[option][0]} são {alunos[option][1]}')
        else:
            print('Aluno inválido, digite novamente.')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')