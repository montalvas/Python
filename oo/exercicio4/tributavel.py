import abc


class Tributavel(abc.ABC):
    """
    Classe que contém operações de um objeto autenticável
    As subclasses concretas devem sobrescrever o método get_valor_imposto
    """

    @abc.abstractmethod
    def get_valor_imposto(self):
        """ Aplica taxa de imposto sobre um determinado valor do objeto """
        pass


class SeguroDeVida(Tributavel):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        self._titular = value

    @property
    def numero_apolice(self):
        return self._numero_apolice

    @numero_apolice.setter
    def numero_apolice(self, value):
        self._numero_apolice = value

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05


class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for tributo in lista_tributaveis:
            if isinstance(tributo, Tributavel):
                total += tributo.get_valor_imposto()
            else:
                print(tributo.__repr__(), 'não é um tributável')
        return total
