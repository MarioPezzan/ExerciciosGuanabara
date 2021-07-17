a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))
e = int(input('Digite o quinto valor: '))
menor = a
if b < a and b < c and b < d and b < e:
    menor = b
if c < a and c < b and c < d and c < e:
    menor = c
if d < a and d < b and d < c and d < e:
    menor = d
if e < a and e < b and e < c and e < d:
    menor = e
if a < b and a < c and a < d and a < e:
    menor = a
maior = a
if b > a and b > c and b > d and b > e:
    maior = b
if c > a and c > b and c > d and c > e:
    maior = c
if d > a and d > b and d > c and d > e:
    maior = d
if e > a and e > b and e > c and e > d:
    maior = e
if a > b and a > c and a > d and a > e:
    maior = a
print(f'O menor valor digitado é {menor}')
print(f'O maior valor digitado é {maior}')
