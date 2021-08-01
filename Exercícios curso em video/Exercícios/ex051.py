n = int(input('Digite o primeio número: '))
r = int(input('Digite a razão: '))
an = n+(10-1)*r
for c in range(n, an, r):
    print(c, end=(' -> '))
print('ACABOU')