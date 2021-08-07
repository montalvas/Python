class Conta:
    __slots__ = ['_numero', '_titular', '_saldo']

    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

nova_conta = Conta('123-5', 'Lucas', 5000)
nova_conta.transacoes = 5 # Não permite a criação de novos atríbutos