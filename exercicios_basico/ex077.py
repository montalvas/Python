# Mostrar as vogais de um conjunto de palavras

conjunto = ('abacate', 'amizade', 'bateria', 'bigode', 'cadeira', 'comida', 'dezenove', 'educado',
            'feriado', 'goiaba', 'habilidade', 'inimigo', 'jabuticaba', 'jenipapo', 'limonada')
for palavra in conjunto:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    print('')