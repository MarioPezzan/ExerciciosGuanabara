from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa do triangulo retangulo com o cateto oposto {co} e cateto adjacente {ca} é igual a {hi:.2f}')
