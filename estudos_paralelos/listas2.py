pessoas = [['Lucas', 26], ['Adriana', 27], ['Miguel', 3]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2])
for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')