soma = num = 0
while True:
    num = int(input('Digite um valor (Digite 999 para parar): '))
    if num == 999:
        break
    soma += num
print(f'A soma dos valores digitados foi {soma}')
