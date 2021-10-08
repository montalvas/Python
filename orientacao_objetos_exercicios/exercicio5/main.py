from excecoes import SaldoInsuficienteError
from conta import ContaCorrente, ContaPoupanca, ContaInvestimento
from caixa import CaixaEletronico

cc = ContaCorrente('123-1', 'João', 1000)
cp = ContaPoupanca('123-5', 'José', 0)
value = -1000
caixa = CaixaEletronico()

caixa.deposita(cc, value)
caixa.saca(cc, value)

value = 5000
caixa.saca(cc, value)

value = 300
caixa.transfere(cc, value, cp)