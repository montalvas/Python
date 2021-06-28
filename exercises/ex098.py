def contador(i, f, p):
    print('-=' * 20)
    if i < f:
        print('Calculando: ', end='')
        while i <= f:
            print(i, end=' ')
            i += p
    elif i > f:
        print('Calculando: ', end='')
        while i >= f:
            print(i, end=' ')
            i -= p
    print('FIM.')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de realizar uma contagem personalizada')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio < fim:
    if passo == 0 or passo > (fim - inicio):
        passo = 1
    elif (-1 * (fim - inicio)) <= passo < 0:
        passo *= -1
    contador(inicio, fim, passo)
elif inicio > fim:
    if passo == 0 or passo > (inicio - fim):
        passo = 1
    elif (-1 * (inicio - fim)) <= passo < 0:
        passo *= -1
    contador(inicio, fim, passo)
else:
    print(f'{inicio} = {fim}, logo não é possível contar!')
