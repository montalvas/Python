from conta import ContaCorrente, ContaPoupanca, ContaInvestimento
from tributavel import Tributavel, SeguroDeVida, ManipuladorDeTributaveis

conta1 = ContaCorrente('123-5', 'João')
conta1.deposita(1000)

seguro1 = SeguroDeVida(100, 'José', '345-75')

conta2 = ContaPoupanca('123-9', 'Maria', 500)

conta3 = ContaInvestimento('124-1', 'João', 700)

Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)
Tributavel.register(ContaInvestimento)

print('Imposto conta corrente: {:.2f}'.format(conta1.get_valor_imposto()))
print('Imposto seguro: {:.2f}'.format(seguro1.get_valor_imposto()))
print('Imposto conta investimento: {:.2f}'.format(conta3.get_valor_imposto()))
print('-' * 15)

lista_tributaveis = [conta1, seguro1, conta2, conta3]

mt = ManipuladorDeTributaveis()
print('Total de imposto calculado: {:.2f}'.format(mt.calcula_impostos(lista_tributaveis)))