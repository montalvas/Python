from excecoes import SaldoInsuficienteError


class CaixaEletronico:
    def deposita(self, conta, valor):
        try:
            conta.deposita(valor)
        except ValueError:
            print('O valor deve ser um número positivo.')
        else:
            print('Depósito realizado com sucesso.')
        finally:
            print('Deseja realizar outra operação?')
            print('-' * 15)

    def saca(self, conta, valor):
        try:
            conta.saca(valor)
        except ValueError:
            print('O valor deve ser um número positivo.')
        except SaldoInsuficienteError:
            print('Saldo insuficiente')
        else:
            print('Saque realizado com sucesso.')
        finally:
            print('Deseja realizar outra operação?')
            print('-' * 15)
    
    def transfere(self, conta, valor, destino):
        try:
            conta.transfere_para(valor, destino)
        except ValueError:
            print('O valor deve ser um número positivo.')
        except SaldoInsuficienteError:
            print('Saldo insuficiente')
        else:
            print(f'Transferência para {destino.titular} realizada com sucesso.')
        finally:
            print('Deseja realizar outra operação?')
            print('-' * 15)
            
