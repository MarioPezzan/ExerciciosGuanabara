listagem = ('Caderno', 10,
            'Lapis', 3.75,
            'Tesoura', 5.50,
            'Cola', 2.60,
            'Estojo', 6.99)
for prot in range(0, len(listagem)):
    if prot % 2 == 0:
        print(f'{listagem[prot]:.<30}', end='')
    else:
        print(f'R$ {listagem[prot]:.2f}')