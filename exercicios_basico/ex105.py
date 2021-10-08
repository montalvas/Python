def notas(*conjunto, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param conjunto: uma ou mais notas dos alunos.
    :param sit: (Opcional) Adicionar ou não a situação.
    :return: Um dicionário contendo várias informações sobre a situação da turma.
    '''
    dados = dict()
    maior = menor = media = 0
    for nota in conjunto:
        media += nota
        if conjunto.index(nota) == 0:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
    dados['quantidade'] = len(conjunto)
    dados['maior'] = maior
    dados['menor'] = menor
    dados['média'] = media/len(conjunto)
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] >= 6:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


print(notas(3.5, 2, 6.5, 2, 7, 4, sit=True))
help(notas)