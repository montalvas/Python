from collections.abc import MutableSequence
from conta import Conta, ContaCorrente

class Contas(MutableSequence):
    _dados = []
    
    def __len__(self):
        return len(self._dados)
    
    def __getitem__(self, key):
        return self._dados[key]

    def __setitem__(self, key, value):
        if isinstance(value, Conta):
            self._dados[key] = value
        else:
            raise TypeError("valor atribuido não é uma conta")
    
    def __delitem__(self, key):
        del self._dados[key]
    
    def insert(self, key, value):
        if isinstance(value, Conta):
            self._dados.insert(key, value)
        else:
            raise TypeError('valor inserido não é uma conta')
    


if __name__ == '__main__':
    import csv
    
    contas = Contas()
    
    arquivo = open('contas.txt', 'r')
    leitor = csv.reader(arquivo)
    
    for linha in leitor:
        conta = ContaCorrente(linha[0], linha[1], float(linha[2]), float(linha[3]))
        contas.append(conta)
    arquivo.close()
    
    print('saldo - imposto')
    for c in contas:
        print(f'{c.saldo} - {c.get_valor_imposto()}')