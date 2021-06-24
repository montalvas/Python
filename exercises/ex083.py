# Verifique o parênteses da expressão

parenteses = list()
aberto = list()
fechado = list()
expressao = input('Digite a expressão: ')
for pos, val in enumerate(expressao):
    if val == '(':
        aberto.append(pos)
    elif val == ')':
        fechado.append(pos)
if len(aberto) != len(fechado):
    print('Expressão está inválida!')
else:
    res = 'Expressão está válida!'
    for p in range(0, len(aberto)):
        if aberto[p] > fechado[p]:
            res = 'Expressão está inválida!'
            break
    print(res)