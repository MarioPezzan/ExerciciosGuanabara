from random import randint
from time import sleep
escolhido = randint(1, 10)
n1 = 0
n2 = 0
while escolhido != n1:
    n1 = int(input('tente acertar o numero de 1 a 10 escolhido pelo o computador: '))
    if n1 <= 10:
        print('PROCESSANDO...')
        sleep(2)
        if n1 < escolhido:
            print('Mais! tente mais uma vez')
        elif n1 > escolhido:
            print('Menos! tente novamente')
    else:
        print('Entre 1 a 10! digite novamente')
    n2 += 1
if n1 == escolhido:
    if n2 == 1:
        print('Parabéns!!!! de primeira! Você é o cara! ')
    elif n2 == 5:
        print(f'Parabéns você acertou o número escolhido na {n2}° tentativa!')
    elif n2 < 10:
        print(f'Poxa Errou bastante em! foram {n2}° tentativas mas conseguiu acertar!')
    else:
        print('Você excedeu o limite de tentativas :(')
