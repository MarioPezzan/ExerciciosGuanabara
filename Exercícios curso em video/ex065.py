c = soma = n = menor = maior = 0
n1 = ''
while not n1 == 'N':
    n = int(input('Digite um numero: '))
    n1 = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if n1 != 'N' or 'S':
        soma += n
        c += 1
        if c == 1:
            menor = maior = c
        else:
            if n < menor:
                menor = n
            if n > maior:
                maior = n
    else:
        print('Valor invalido')
print(f'''Você digitou {c} números e a media entre eles são {soma/c:.2f} 
O menor valor digitado é {menor}
O maior valor digitado é {maior}''')