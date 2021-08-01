time = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
        'Grêmio', 'Palmeiras', 'Santos', 'Athletico Paranaense', 'Red Bull Bragantino',
        'Ceará', 'Corinthians',  'Atlético-Go', 'Bahia', 'Sport',
        'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('\033[1;34mTABELA BRASILEIRÃO 2020\033[m')
print(f'Os 5 primeiros times são: {time[0:5]}')
print(f'Os últimos 4 colocados são: {time[-4:]}')
print(f'Todos os times organizados em ordem alfabetica: {sorted(time)}')
print(f'A posição do São Paulo na tabela: {time.index("São Paulo")+1}ª')
