class Cliente:
    __slots__ = ['_nome', '_sobrenome', '_cpf', '_id']

    id = 0

    @classmethod
    def get_id(cls):
        return cls.id

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        Cliente.id += 1
        self._id = Cliente.id

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf

    def mostrar_dados(self):
        print(f'ID_CLIENTE: {self._id}')
        print(f'Cliente: {self.nome} {self.sobrenome}')
        print(f'CPF: {self.cpf}')