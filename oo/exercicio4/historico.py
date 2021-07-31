import datetime


class Historico:
    __slots__ = ['_data_abertura', '_transacoes']

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    @property
    def data_abertura(self):
        return self._data_abertura

    @property
    def transacoes(self):
        return self._transacoes

    def abertura(self):
        print(f'Abertura da conta em: {self.data_abertura}')

    def nova_transacao(self, t):
        self.transacoes.append(t)

    def mostrar_transacoes(self):
        print('Extrato:')
        for transacao in self.transacoes:
            print(f'- {transacao}')