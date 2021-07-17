m = int(input('Até que número deseja? '))
an = 1+(m-1)*2
for c in range(1, an + 1, 2):
    print(c, end=(' -> '))
print('ACABOU')