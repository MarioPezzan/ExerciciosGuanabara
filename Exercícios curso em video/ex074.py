from random import randint
tupla = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5),)
for c in tupla:
    print(c, end=' ')
print(f'\nO maior número é {max(tupla)}')
print(f'O menor número é {min(tupla)}')


