"""
    Leia uma frase e mostre:
    a) Quantas vezes aparece a letra 'A'.
    b) Em qual posição ela aparece na 1ª vez.
    c) Em qual posição ela aparece pela última vez.
"""

frase = input("Digite uma frase qualquer: ")
q = (frase.lower()).count('a')
print("A quantidade de letras 'a' é: ", q)

first = (frase.lower()).find('a')
print("A posição em que aparece pela primeira vez é: ", first)

last = (frase.lower()).rfind('a')
print('A posição em que aparece pela última vez é: ', last)
