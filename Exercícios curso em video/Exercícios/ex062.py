n = int(input('Digite o valor de n: '))
r = int(input('Digite o valor da razão: '))
c = n
q = 11
v = q
while not c == n+(q-1)*r and q != 0:
    print(c, end=' > ')
    c += r
    if c == n+(q-1)*r:
        n = c
        print('PAUSA')
        q = int(input('quantos termos deseja a mais? '))
        q += 1
        v += q - 1
print(f'Progressão finalizada com {v-1} termos mostrados')