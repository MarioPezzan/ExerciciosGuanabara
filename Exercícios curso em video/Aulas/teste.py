print('''Cada antena está posicionada numa coordenada Pa=(Xa,Ya) definida em
metros, e toda a cobertura da antena é dada pelo círculo definido por R, em metros. 
Para verificar se um ponto Q=(xq, yq) da cidade (em metros) está coberto pela antena, ela 
precisa satisfazer a condição:\n''')
'\\ (Xq-Xa)² + (Yq-Ya)² <= R2\n'
print('''A antena 1 está localizada na posição A1=(15200,11901) e o seu raio de alcance é R1=800m.
A antena 2 está localizada na posição A2=(16093,12287) e o seu raio de alcance é R2=700m.''')
print('Digite as Cordenada que deseja conferir:')
Xq = int(input('Xq: '))
Yq = int(input('Yq: '))
A2 = (Xq - 16093)**2 + (Yq - 12287)**2
A1 = (Xq - 15200)**2 + (Yq - 11901)**2
'\\ boa noite'
if A1 <= 800**2:
    print(f'A antena A1 localizada na posição A1=(15200,11901) cobrirá o ponto Q=({Xq},{Yq})')
else:
    print(f'A antena A1 localizada na posição A1=(15200,11901) não cobrirá o ponto Q=({Xq},{Yq})')
if A2 <= 800**2:
    print(f'A antena A2 localizada na posição A1=(16093,12287) cobrirá o ponto Q=({Xq},{Yq})')
else:
    print(f'A antena A2 localizada na posição A1=(16093,12287) não cobrirá o ponto Q=({Xq},{Yq})')