listagem = []
n = ''
while n != 'N':
    listagem.append(int(input('Digite um valor: ')))
    for v in listagem:
        if listagem.count(v) > 1:
            print('Esse valor está duplicado, portanto não irei adiciona-lo')
            listagem.pop()
            break
    print('Valor adicionado com sucesso')
    n = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
listagem.sort()
print(listagem)

#forma alternativa guanabara
numero = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
numero.sort()
print(f'Você digitou os valores {numero}')