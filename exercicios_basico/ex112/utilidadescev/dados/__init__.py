def leiaDinheiro(q):
    while True:
        p = (input(q)).strip()
        if p.isalpha() or p == '':
            print(f'\033[31mERRO: "{p}" é um preço inválido!\033[m')
        else:
            if ',' in p:
                p = p.replace(',', '.')
            break
    return float(p)