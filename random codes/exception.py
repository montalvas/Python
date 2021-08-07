try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro}')
else:
    print(f'O resultado é {r}')
finally:
    print('O comando foi executado!')