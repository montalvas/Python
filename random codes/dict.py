filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.keys())
print(filme.values())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'wachowski'}
            ]
print(locadora[1]['titulo'])
for f in locadora:
    for k, v in f.items():
        print(f'{k} : {v}.', end=' ')
    print('')