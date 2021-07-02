def voto():
    from datetime import datetime
    print('-' * 20)
    ano = int(input('Em que ano você nasceu? '))
    idade = datetime.now().year - ano
    if 18 <= idade < 65:
        res = 'VOTO OBRIGATÓRIO'
    elif idade >= 16 or idade >= 65:
        res = 'VOTO OPCIONAL'
    else:
        res = 'NÃO VOTA'
    print(f'Com {idade} anos: {res}')


voto()