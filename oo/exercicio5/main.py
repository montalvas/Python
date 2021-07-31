from excecoes import SaldoInsuficienteError
from conta import ContaCorrente, ContaPoupanca, ContaInvestimento

cc = ContaCorrente('123-1', 'João', 1000)
value = -1000
try:
    cc.saca(value)
    print(f'Valor {value} sacado com sucesso.')
except ValueError:
    print('O valor a ser sacado deve ser um número positivo.')

value = 5000
try:
    cc.saca(value)
    print(f'Valor {value} sacado com sucesso.')
except ValueError:
    print('O valor a ser sacado deve ser um número positivo.')
except SaldoInsuficienteError:
    print('Você não possui saldo suficiente.')