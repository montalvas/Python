from conta import Conta, ContaCorrente, ContaPoupanca
from atualizador import AtualizadorDeContas

c = Conta('123-5', 'Lucas', 1000)
cc = ContaCorrente('123-3', 'Adriana', 1000)
cp = ContaPoupanca('123-1', 'Miguel', 1000)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print(c.saldo)
print(cc.saldo)
print(cp.saldo)
print('=' * 20)

print(c)
print('=' * 20)

att = AtualizadorDeContas(0.01)

att.iniciar(c)
att.iniciar(cc)
att.iniciar(cp)
print(f'Saldo total: {att.saldo_total}')