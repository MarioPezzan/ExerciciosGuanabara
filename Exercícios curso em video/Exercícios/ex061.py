n = int(input('Digite o valor de n: '))
r = int(input('Digite o valor da razão: '))
c = n
q = 11
v = q
while not c == n+(q-1)*r and q != 0:
    print(c, end=' > ')
    c += r
print(f'FIM')