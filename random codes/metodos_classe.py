class Conta:
    _total_contas = 0

    def __init__(self):
        type(self)._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

conta1 = Conta()
conta2 = Conta()
print(f'Total de contas(acessado pelo objeto): {conta1.get_total_contas()}')
print(f'Total de contas(acessado pela classe): {Conta.get_total_contas()}')
