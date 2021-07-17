from math import sqrt
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = b**2 - 4*a*c
if delta < 0:
    print('esta equação não possui raízes reais')
if delta == 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    print(f'a raiz desta equação é {x1}')
elif delta > 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    if x1 > x2:
        print(f'as raízes da equação são {x2:.2f} e {x1:.2f}')
    else:print(f'as raízes da equação são {x1:.2f} e {x2:.2f}')
