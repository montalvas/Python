from historico import Historico


class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_historico', '_id']

    id = 0

    @classmethod
    def get_id(cls):
        return cls.id

    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._historico = Historico()
        Conta.id += 1
        self._id = Conta.id

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo > 0:
            self._saldo = saldo

    @property
    def historico(self):
        return self._historico

    def mostrar_abertura_conta(self):
        print('=' * 20)
        self.historico.abertura()
        self.titular.mostrar_dados()
        print(f'Conta número: {self.numero}')

    def extrato(self):
        print('=' * 20)
        self.historico.mostrar_transacoes()
        print('Saldo: R$ {:.2f}'.format(self.saldo))

    def deposita(self, valor):
        self.saldo += valor
        self.historico.nova_transacao('Depósito: {:.2f}'.format(valor))

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.nova_transacao('Saque: {:.2f}'.format(valor))
        else:
            print(f'Operação não realizada.')

    def transfere_para(self, valor, destino):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            self.historico.nova_transacao('Transferência: {:.2f} para conta {}'.format(valor, destino.numero))
        else:
            print('Operação não realizada.')

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        return "Dados da conta: \nNúmero: {} \nTitular: {} \nSaldo: {}".format(self._numero, self._titular, self._saldo)


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self.saldo += valor - 0.10
        self.historico.transacoes.append(f'depósito de {valor}')


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
