n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=(' '))
        total += 1
    else:
        print('\033[31m', end=(' '))
    print(f'{c}', end=(' '))
print(f'\n\033[mO número {n} é divisivél por {total} números', end=' ')
if total == 2:
    print('e por tanto ele é um número PRIMO!')
else:
    print('e por tanto ele não é um número PRIMO!')