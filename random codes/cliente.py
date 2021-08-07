class Cliente:
    _total_clientes = 0

    @classmethod
    def get_total_clientes(cls):
        return cls._total_clientes

    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
        Cliente._total_clientes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def sexo(self):
        return self._sexo

    def altera_nome(self, value):
        self._nome = value

    def altera_idade(self, value):
        self._idade = value

    def altera_sexo(self, value):
        self._sexo = value

    def dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Sexo: {self.sexo}')

cliente = Cliente('Lucas', 26, 'M')
cliente2 = Cliente('Miguel', 4, 'M')
nome = cliente.nome
idade = cliente.idade
sexo = cliente.sexo
print(f'Nome: {nome} \nIdade: {idade} \nSexo: {sexo}')
cliente.altera_nome('Adriana')
cliente.altera_idade(27)
cliente.altera_sexo('F')
print('=' * 15)
print('Dados do cliente:')
cliente.dados()
print('=' * 15)
print(f'Total clientes: {Cliente.get_total_clientes()}')
print(f'Outra forma de mostrar o total: {cliente.get_total_clientes()}')