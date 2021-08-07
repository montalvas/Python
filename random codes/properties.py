class Pessoa:
    def __init__(self, nome=''):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

pessoa1 = Pessoa('Miguel')
pessoa1.nome = 'Lucas'
print(pessoa1.nome)