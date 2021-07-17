from math import sqrt
print('Digite as cordenadas do primeiro ponto cartesiano')
x1 = float(input('Digite o valor de x1: '))
y2 = float(input('Digite o valor de y2: '))
print('Digite as cordenadas do segundo ponto cartesiano')
x3 = float(input('Digite o valor de x1: '))
y4 = float(input('Digite o valor de y2: '))
d = (x1-x3)**2 + (y2-y4)**2
if sqrt(d) >= 10:
    print('longe')
else:
    print('perto')
