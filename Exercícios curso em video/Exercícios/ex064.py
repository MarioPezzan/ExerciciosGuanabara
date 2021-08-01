c = cn = n = 0
while not n == 999:
    n = int(input('Digite um numero [Digite 999 para parar]: '))
    if n != 999:
        cn += n
        c += 1
print(f'A soma dos {c} valores que você digitou é igual a {cn}')