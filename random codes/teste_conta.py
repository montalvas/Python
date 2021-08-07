# Forma procedural de criar uma conta
def cria_conta(numero, titular, saldo, limite):
    '''
    -> Cria uma conta bancária
    :param numero: número da conta bancária (string)
    :param titular: nome do titular (string)
    :param saldo: saldo inicial da conta (float)
    :param limite: limite de saldo da conta (float)
    :return: retorna um dicionário
    '''
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    '''
    -> Deposita um valor no saldo da conta
    :param conta: conta a ser passada
    :param valor: valor a ser adicionado ao saldo
    :return: sem retorno
    '''
    conta['saldo'] += valor


def saca(conta, valor):
    '''
    -> Saca um valor no saldo da conta
    :param conta: conta a ser passada
    :param valor: valor a ser subtraido do saldo
    :return: sem retorno
    '''
    conta['saldo'] -= valor


def extrato(conta):
    '''
    -> Imprimi o número e o saldo da conta
    :param conta: conta a ser passada
    :return: sem retorno
    '''
    print('Número: {} \nSaldo: R$ {:.2f}'.format(conta['numero'], conta['saldo']))


conta1 = cria_conta('123-7', 'João', 500, 1000)
deposita(conta1, 200)
saca(conta1, 300)
extrato(conta1)