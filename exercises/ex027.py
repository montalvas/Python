# Ler o nome completo e dizer o primeiro e último nome

name = input("Digite seu nome completo: ")
print("Nome completo: ", name)

name = name.split()
first = name[0]
last = name[len(name) - 1]
print("Primeiro nome: ", first)
print("Último nome: ", last)
