# Informe um número e em seguida mostre seu dobro, triplo e sua raiz.

n = int(input("Informe um número: "))
double = n * 2
triple = n * 3
raiz = n ** (1/2)
print('O número digitado foi {}\nSeu dobro é {}\nSeu triplo é {}\nSua raiz é {:.2f}'.format(n, double, triple, raiz))
