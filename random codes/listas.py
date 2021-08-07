# Parte prática de listas

num = [2, 5, 9, 1]
num[2] = 8
print(num)

#num[4] = 7 -> gera erro
num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(1, 3)
print(num)

num.pop()
print(num)

print(max(num))
print(min(num))

if 2 in num:
    num.remove(2)
print(num)

for n in num:
    print(n, end=' ')