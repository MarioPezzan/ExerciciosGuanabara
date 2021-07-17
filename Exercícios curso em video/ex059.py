print('-='*15)
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
n1 = 0
while not n1 == 5:
    print('''Escolha uma das operações 
[ 1 ] Somar
[ 2 ] Mutiplicar
[ 3 ] Maior número
[ 4 ] Novos números 
[ 5 ] Sair do programa ''')
    n1 = int(input('>>>>> Qual sua opção? '))
    if n1 < 6:
        if n1 == 1:
            print(f'A soma entre {primeiro} + {segundo} é {primeiro+segundo}')
        elif n1 == 2:
            print(f'A multiplicação entre {primeiro} X {segundo} é {primeiro*segundo}')
        elif n1 == 3:
            if primeiro > segundo:
                print(f'O número {primeiro} é o maior')
            elif primeiro == segundo:
                print(f'Não á um maior os dois números são iguais')
            else:
                print(f'O número {segundo} é maior')
        elif n1 == 4:
            primeiro = int(input('Digite o primeiro valor: '))
            segundo = int(input('Digite o segundo valor: '))
    else:
        print('Digite uma opção valida!')
    print('-==' * 15)
print('Obrigado por usar o programa')