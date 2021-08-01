from random import randint
cont = 0
while True:
    numero = int(input('Digite um número: '))
    par_impar = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
    n_computador = randint(0, 10)
    soma_numeros = n_computador + numero
    resultado = soma_numeros % 2
    while par_impar not in 'IP':
        par_impar = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
    print(f'Você escolheu {numero} e o computador {n_computador} portanto deu {numero+n_computador} ')
    if resultado == 1 and par_impar == 'I':
        print(f'Você ganhou!')
        print('Vamos jogar novamente...')
    if resultado == 0 and par_impar == 'P':
        print(f'Você ganhou!')
        print('Vamos jogar novamente...')
    if resultado == 1 and par_impar == 'P':
        break
    if resultado == 0 and par_impar == 'I':
        break
    cont += 1
print(f'Você perdeu! foram {cont} vitoria!')
print('GAME OVER!')
