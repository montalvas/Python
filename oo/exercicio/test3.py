from conta import ContaCorrente, ContaPoupanca
from atualizador import AtualizadorDeContas
from cliente import Cliente

cc = ContaCorrente('1', 'M', 100)
cp = ContaPoupanca('2', 'L', 100)
att = AtualizadorDeContas(0.10)

att.iniciar(cc)
att.iniciar(cp)

cl = Cliente('L', 'M', '111')
att.iniciar(cl)