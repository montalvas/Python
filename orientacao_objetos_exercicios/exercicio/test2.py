from conta import Conta, ContaCorrente, ContaPoupanca
from banco import Banco
from atualizador import AtualizadorDeContas

cc1 = ContaCorrente('1', 'Miguel', 1000)
cc2 = ContaCorrente('2', 'Luna', 500)
cp1 = ContaPoupanca('3', 'Apolo', 100)
cp2 = ContaPoupanca('4', 'Natalie', 200)
cc3 = ContaCorrente('5', 'Lucas', 1000)
cp3 = ContaPoupanca('6', 'Adriana', 500)

inter = Banco()
inter.adiciona(cc1)
inter.adiciona(cc2)
inter.adiciona(cp1)
inter.adiciona(cp2)
inter.adiciona(cc3)
inter.adiciona(cp3)

print(f'Total de contas cadastradas: {inter.pegaTotalDeContas()}\n')
print(f'Conta na posição 0: \n{inter.pegaConta(0)}\n')
print(f'Conta na posição 6: {inter.pegaConta(6)}\n')

att = AtualizadorDeContas(0.10)
for conta in inter._lista_de_contas:
    att.iniciar(conta)