from datetime import datetime

ctps = dict()
ctps['nome'] = input('Nome: ')
idade = int(input('Ano de nascimento: '))
ctps['idade'] = datetime.now().year - idade
ctps['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if ctps['carteira'] != 0:
    ctps['contratacao'] = int(input('Ano de contratação: '))
    ctps['salario'] = float(input('Salário: R$ '))
    ctps['aposentadoria'] = ctps['idade'] + 35 - (datetime.now().year - ctps['contratacao'])
print('-=' * 30)
print(ctps)
for k, v in ctps.items():
    print(f'O {k} tem o valor {v}')
