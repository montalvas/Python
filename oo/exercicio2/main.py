from conta import ContaCorrente, ContaPoupanca, ContaInvestimento

cc = ContaCorrente('123-5', 'Lucas', 1000)
cp = ContaPoupanca('123-1', 'Adriana', 1000)
ci = ContaInvestimento('123-9', 'Miguel', 1000)

cc.atualiza(0.05)
cp.atualiza(0.01)
ci.atualiza(0.01)

print(cc)
print(cp)
print(ci)