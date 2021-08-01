soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite {c}° número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A quantidade de números pares são igual a {cont} e a soma deles é igual a {soma}')