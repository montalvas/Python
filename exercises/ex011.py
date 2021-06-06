# Ler largura e altura de uma parede e descobrir a quantidade de tinta necessária para pinta-la
# Sabendo-se que cada litro de tinta pinta 2m² de parede.

lag = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lag * alt
print('A área de uma parede {} x {} é igual a {} m².\nPara pintá-la serão necessários {} l de tinta.'.format(lag, alt, area, area/2))