from banco.conta import Conta
from banco.cliente import Cliente

conta1 = Conta('123-4', 'João', 120)
conta2 = Conta('123-5', 'Guilherme', 0)
conta1.deposita(100)
conta1.extrato()
operacao = conta1.saca(300)
if operacao:
    print('Saque efetuado com sucesso!')
else:
    print('Saldo insuficiente!')
conta1.transfere_para(conta2, 120)
cliente1 = Cliente('Miguel', 'Montalvani', '1234')
conta3 = Conta('123-9', cliente1, 150)
print(conta3.titular.nome)