import abc


class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario=0):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value

    @abc.abstractmethod
    def get_bonificacao(self):
        pass


class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if hasattr(obj, 'get_bonificacao'):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(f'Instância de {self.__class__.__name__} não implementa o método get_bonificacao()')


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    def get_bonificacao(self):
        return self._salario * 0.15


if __name__ == '__main__':
    g = Gerente('Jose', '111', 5000, '1234')
    print(g.salario)
