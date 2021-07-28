import abc
from tributavel import Tributavel
from historico import Historico


class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._tipo = self.__class__.__name__

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        self._titular = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        self._limite = value

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

    def __str__(self):
        return "Dados da conta: \nTipo: {} \nNúmero: {} \nTitular: {} \nSaldo: {} \n\n".format(self._tipo, self._numero,
                                                                                               self._titular, self._saldo)

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass


class ContaCorrente(Conta, Tributavel):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self.saldo += valor - 0.10
        self.historico.transacoes.append(f'depósito de {valor}')

    def get_valor_imposto(self):
        return self.saldo * 0.01


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 5
