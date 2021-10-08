# Leia um valor em metros e em seguida exiba convertido em centímetros e milímetros.

m = float(input('Digite o comprimento em metros: '))
cm = m * 100
mm = m * 1000
print('O valor {} m pode ser convertido em {} cm ou {} mm.'.format(m, cm, mm))