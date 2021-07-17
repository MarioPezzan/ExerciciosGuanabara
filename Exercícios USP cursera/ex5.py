print('Digite uma sequência de  numeros inteiros de 0 a 9999')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Teceiro número: '))
an = n1+(4-1)*1
if an == n3+1:
    print(f'A sequência dos números {n1}, {n2}, {n3} representa uma sequência crescente!')
else:
    print(f'Os números {n1}, {n2}, {n3} não representa uma sequência crescente!')
