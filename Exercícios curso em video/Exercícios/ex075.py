n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Mais um número: '))
n4 = int(input('O ultimo número: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 aparece na {(tupla.index(3)+1)}ª posição ')
else:
    print('Não tem o número 3 dentro dos valores digitados')
print('Os valores pares digitados foram', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

