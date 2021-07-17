import random
from time import sleep
print(f"\033[1;30;41m{12*'-='}JOKENPÔ{13*'=-'}\033[m")
print("""\033[1;36mEsolha sua jogada:
[1]PEDRA
[2]PAPEL
[3]TESOURA""")
escolhido = int(input('Digite o número de sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!')
print(f"\033[1;30;41m{26*'-='}{1*'=-'}\033[m")
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
if computador == 'pedra' and escolhido == 2:
    print(f'\033[1;35mParabéns você ganhou! A maquina escolheu {computador}\033[m')
elif computador == 'pedra' and escolhido == 3:
    print(f"\033[1;35mHAHA Eu ganhei! eu escolhi {computador}!\033[m")
elif computador == 'pedra' and escolhido == 1:
    print(f'\033[1;35mOpa a maquina também escolheu {computador}, tente novamente!\033[m')
if computador == 'papel' and escolhido == 3:
    print(f'\033[1;35mParabéns você ganhou! A maquina escolheu {computador}\033[m')
elif computador == 'papel' and escolhido == 1:
    print(f'\033[1;35mHAHA Eu ganhei! eu escolhi {computador}!\033[m')
elif computador == 'papel' and escolhido == 2:
    print(f'\033[1;35mOpa a maquina também escolheu {computador}, tente novamente!\033[m')
if computador == 'tesoura' and escolhido == 1:
    print(f'\033[1;35mParabéns você ganhou! A maquina escolheu {computador}\033[m')
elif computador == 'tesoura' and escolhido == 2:
    print(f'\033[1;35mHAHA Eu ganhei! eu escolhi {computador}!\033[m')
elif computador == 'tesoura' and escolhido == 3:
    print(f'\033[1;35mOpa a maquina também escolheu {computador}, tente novamente!\033[m')
elif escolhido > 3:
    print(f"\033[1;36;41m{'VALOR INVALIDO!':^54}\033[m")
print(f"\033[1;30;41m{26*'-='}{1*'=-'}\033[m")
