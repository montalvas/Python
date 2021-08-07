conteudo = []
try:
    arquivo = open('arquivo.txt')
except FileNotFoundError:
    arquivo = open('arquivo.txt', 'w')
else:
    for linha in arquivo:
        linha = linha.strip()
        conteudo.append(linha)
print(conteudo[0])
print(f'Quantidade de linhas {len(conteudo)}')