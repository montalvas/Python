from random import randint

numeros = list()

def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(1, 100))
    print(f'Foram sorteados os números {lst}')


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos pares vale {soma}')


sorteia(numeros)
somaPar(numeros)