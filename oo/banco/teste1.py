from banco.conta import Conta
from banco.cliente import Cliente

cliente1 = Cliente('João', 'Oliveira', '111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000)
conta2 = Conta('123-5', cliente2, 1000)
conta1.deposita(100)
conta1.saca(50)
conta1.transfere_para(conta2, 200)
conta1.extrato()
conta1.historico.imprime()
conta2.historico.imprime()