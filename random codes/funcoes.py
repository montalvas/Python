def velocidade_media(distancia, tempo):
    try:
        velocidade = divisao(distancia, tempo)
    except ZeroDivisionError:
        return 'Não pode dividir por zero'
    else:
        return velocidade

def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def calculadora(x, y):
    return x + y, x - y, x * y, x / y


def divisao(x, y):
    return x / y


res = velocidade_media(120, 4)
print(f'A velocidade média é {res} m/s')
print(f'A soma entre 10 e 15 é {soma(10, 15)}')
print(f'A diferença entre 27 e 4 é {subtracao(27, 4)}')
print(f'Os cálculos matemáticos de 5 e 2 são: {calculadora(5, 2)}')
print(f'Velocidade média1: {velocidade_media(100, 20)}')
print(f'Velocidade média2: {velocidade_media(-20, 10)}')
print(f'Velocidade média3: {velocidade_media(150, 0)}')
