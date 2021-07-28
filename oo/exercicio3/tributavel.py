class Tributavel:
    def get_valor_imposto(self):
        pass


class SeguroDeVida(Tributavel):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05  # Taxa de 50 reais + 5% valor do plano


class ManipuladorDeTributaveis:
    def calcula_imposto(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total
