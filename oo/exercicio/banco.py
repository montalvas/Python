class Banco:
    def __init__(self):
        self._lista_de_contas = []
    
    @property
    def lista_de_contas(self):
        return self._lista_de_contas
    
    def adiciona(self, conta):
        self._lista_de_contas.append(conta)
    
    def pegaConta(self, posicao):
        try:
            return self._lista_de_contas[posicao]
        except IndexError:
            return 'Conta não encontrada.'
    
    def pegaTotalDeContas(self):
        return len(self._lista_de_contas)