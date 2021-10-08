from conta import ContaCorrente
from tributavel import Tributavel, SeguroDeVida, ManipuladorDeTributaveis

cc1 = ContaCorrente('123-4', 'João', 1000)
cc2 = ContaCorrente('123-5', 'José', 1000)

seguro1 = SeguroDeVida(100, 'José', '345-77')
seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

lista_tributaveis = []
lista_tributaveis.append(cc1)
lista_tributaveis.append(cc2)
lista_tributaveis.append(seguro1)
lista_tributaveis.append(seguro2)

manipulador = ManipuladorDeTributaveis()
total = manipulador.calcula_imposto(lista_tributaveis)
print(total)
