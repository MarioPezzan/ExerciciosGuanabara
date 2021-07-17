n = int(input('Digite o valor de n: '))
c = n
f = 1
print(end=f'{n}! = ')
while c > 1:
    f *= c
    c -= 1
    print(f'{c + 1} x ', end='')
print('1 =', f)

