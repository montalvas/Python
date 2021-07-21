from banco.historico import Historico


class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    identificador = 1

    @classmethod
    def get_identificador(cls):
        return cls.identificador

    def __init__(self, numero, titular, saldo, limite = 1000):
        print('Inicializando uma conta')
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta.identificador += 1

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
        if saldo >= 0:
            self._saldo = saldo
        else:
            print('Saldo não pode ser negativo')

    @property
    def historico(self):
        return self._historico

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'depósito de {valor}')

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(f'saque de {valor}')
            return True
        else:
            return False

    def extrato(self):
        print(f'Conta: {self.numero}\nSaldo: R$ {self.saldo}')
        self.historico.transacoes.append(f'Tirou extrato - saldo de {self.saldo}')

    def transfere_para(self, destino, valor):
        if self.saldo >= valor:
            operacao = self.saca(valor)
            if operacao:
                destino.deposita(valor)
                self.historico.transacoes.append(f'transferencia de {valor} para conta {destino.numero}')
                print('Transferência concluída')
            else:
                print('Houve um erro.')