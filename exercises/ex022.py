# Ler o nome completo e mostrar:
# Nome em maiúsculo
# Nome em minúsculo
# Total de letras sem espaços
# Total de letras no primeiro nome

name = input('Digite o nome completo: ')
print('Nome em maiúsculo: ', name.upper())
print('Nome em minúsuclo: ', name.lower())

nameSplitted = name.split()
print('Total de letras: ', len(''.join(nameSplitted)))
print('Total de letras no primeiro nome: ', len(nameSplitted[0]))
