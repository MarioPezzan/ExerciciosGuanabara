n = int(input('Digite o valor de n: '))
c = 2
f = 1
g = 0
print(f'{g} - {f}', end=' - ')
while not c == n:
    an = f + g
    print(f'{an} - ', end='')
    g = f
    f = an
    c += 1
print('FIM')
