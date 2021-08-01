import random
from time import sleep
n1 = int(input('tente acertar o numero de 0 a 5 escolhido pelo o computador: '))
print('PROCESSANDO...')
sleep(2)
lista = [1, 2, 3, 4, 5]
escolhido = random.choice(lista)
if n1 == escolhido:
    print('Parabéns você acertou o número escolhido!')
else:
    print(f'Você errou! o numero escolhido foi {escolhido}! tente novamente.')
