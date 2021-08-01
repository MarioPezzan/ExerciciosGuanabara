#A FORMA QUE EU FIZ
listagem = []
for valor in range(0, 5):
    listagem.append(int(input(f'Digite o valor para posição {valor}: ')))
maior = 0
menor = listagem[0]
for c in listagem:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'Os valores digitados voram: {listagem}')
print(f'o menor valor é {menor} e está na posição', end=' ')
for p, v in enumerate(listagem):
    if v == menor:
        print(p, end='...')
print('')
print(f'O maior valor é {maior} e esta na posição', end=' ')
for p, v in enumerate(listagem):
    if v == maior:
        print(p, end='...')

#FORMA ALTERNATIVA DO PROF GUANABARA

listagem = []
maior = menor = 0
for posicao in range(0, 5):
    listagem.append(int(input(f'Digite o valor para posição {posicao}: ')))
    if posicao == 0:
        maior = menor = listagem[posicao]
    if listagem[posicao] > maior:
        maior = listagem[posicao]
    if listagem[posicao] < menor:
        menor = listagem[posicao]
print(f'Os valores digitados voram: {listagem}')
print(f'o menor valor é {menor} e está na posição', end=' ')
for p, v in enumerate(listagem):
    if v == menor:
        print(p, end='...')
print('')
print(f'O maior valor é {maior} e esta na posição', end=' ')
for p, v in enumerate(listagem):
    if v == maior:
        print(p, end='...')
